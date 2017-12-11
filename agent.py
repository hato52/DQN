import chainer
import chainer.functions as F
import chainer.links as L
import chainerrl
import numpy as np
import random
from matplotlib import pyplot

import environment as env

#Q関数の定義
class QFunction(chainer.Chain):
    def __init__(self, obs_size, n_actions, n_hidden_channels = 64):
        super().__init__(
            l0=L.Linear(obs_size, n_hidden_channels),
            l1=L.Linear(n_hidden_channels,n_hidden_channels),
            l2=L.Linear(n_hidden_channels, n_actions)
        )

    def __call__(self, x, test=False):
        h = F.leaky_relu(self.l0(x), slope = 0.2)
        h = F.leaky_relu(self.l1(h), slope = 0.2)
        return chainerrl.action_value.DiscreteActionValue(self.l2(h))

#最適化、パラメータの設定
obs_size = 64
n_actions = 384  #マス目×コマの種類
q_func = QFunction(obs_size, n_actions)

optimizer = chainer.optimizers.Adam(eps = 1e-2)
gamma = 0.95
#explorer = chainerrl.explorers.LinearDecayEpsilonGreedy(start_epsilon = 1.0, end_epsilon = 0.3 , decay_steps = 50000 ,random_action_func = env.random_move)  
explorer = chainerrl.explorers.ConstantEpsilonGreedy(epsilon = 1.0, random_action_func = env.random_move)    
replay_buffer = chainerrl.replay_buffer.ReplayBuffer(capacity=10 ** 5)
phi = lambda x: x.astype(np.float32, copy = False)
optimizer.setup(q_func)
agent = chainerrl.agents.DQN(
    q_func, optimizer, replay_buffer, gamma, explorer, 
    replay_start_size = 500, update_interval = 1, 
    target_update_interval = 100, phi = phi)


#学習ループ
obs = env.reset()
r = 0
done = False

x = np.array([])
y = np.array([])
win_array = np.array([])
win_sum = 0

#agent.load('final_agent')

for cnt2 in range(1):
    turny = 0
    win = 0
    print("試行回数" + str(cnt2+1))
    for cnt in range(1):
        turn = 0 
        while not done:
            action = agent.act_and_train(obs, r)
            obs, r, done, info = env.step(action)
            turn += 1
            if r == 10:
                win += 1
    
        turny += turn
        
        agent.stop_episode_and_train(obs, r, done)
        obs = env.reset()
        r = 0
        done = False  

    x = np.append(x, cnt2)     
    y = np.append(y, turny/1000)
    win_array = np.append(win_array, win)
    win_sum += win
    #agent.save('final_agent')

print("学習終了")
print("勝ち: " + str(win_sum))

pyplot.plot(x, y)
pyplot.show()

pyplot.plot(x, win_array)
pyplot.show()