import PythonChess.chess as chess
import numpy as np
import random
import re

MOVESTYPE_NUM = 383

dict = {"a":8, "b":7, "c":6, "d":5, "e":4, "f":3, "g":2, "h":1}
pieceType = {1:"", 2:"N", 3:"B", 4:"R", 5:"Q", 6:"K"}
movesType = [
    "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8",
    "Na1", "Na2", "Na3", "Na4", "Na5", "Na6", "Na7", "Na8",
    "Ba1", "Ba2", "Ba3", "Ba4", "Ba5", "Ba6", "Ba7", "Ba8",
    "Ra1", "Ra2", "Ra3", "Ra4", "Ra5", "Ra6", "Ra7", "Ra8",
    "Qa1", "Qa2", "Qa3", "Qa4", "Qa5", "Qa6", "Qa7", "Qa8",
    "Ka1", "Ka2", "Ka3", "Ka4", "Ka5", "Ka6", "Ka7", "Ka8",

    "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8",
    "Nb1", "Nb2", "Nb3", "Nb4", "Nb5", "Nb6", "Nb7", "Nb8",
    "Bb1", "Bb2", "Bb3", "Bb4", "Bb5", "Bb6", "Bb7", "Bb8",
    "Rb1", "Rb2", "Rb3", "Rb4", "Rb5", "Rb6", "Rb7", "Rb8",
    "Qb1", "Qb2", "Qb3", "Qb4", "Qb5", "Qb6", "Qb7", "Qb8",
    "Kb1", "Kb2", "Kb3", "Kb4", "Kb5", "Kb6", "Kb7", "Kb8",

    "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8",
    "Nc1", "Nc2", "Nc3", "Nc4", "Nc5", "Nc6", "Nc7", "Nc8",
    "Bc1", "Bc2", "Bc3", "Bc4", "Bc5", "Bc6", "Bc7", "Bc8",
    "Rc1", "Rc2", "Rc3", "Rc4", "Rc5", "Rc6", "Rc7", "Rc8",
    "Qc1", "Qc2", "Qc3", "Qc4", "Qc5", "Qc6", "Qc7", "Qc8",
    "Kc1", "Kc2", "Kc3", "Kc4", "Kc5", "Kc6", "Kc7", "Kc8",

    "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8",
    "Nd1", "Nd2", "Nd3", "Nd4", "Nd5", "Nd6", "Nd7", "Nd8",
    "Bd1", "Bd2", "Bd3", "Bd4", "Bd5", "Bd6", "Bd7", "Bd8",
    "Rd1", "Rd2", "Rd3", "Rd4", "Rd5", "Rd6", "Rd7", "Rd8",
    "Qd1", "Qd2", "Qd3", "Qd4", "Qd5", "Qd6", "Qd7", "Qd8",
    "Kd1", "Kd2", "Kd3", "Kd4", "Kd5", "Kd6", "Kd7", "Kd8",

    "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8",
    "Ne1", "Ne2", "Ne3", "Ne4", "Ne5", "Ne6", "Ne7", "Ne8",
    "Be1", "Be2", "Be3", "Be4", "Be5", "Be6", "Be7", "Be8",
    "Re1", "Re2", "Re3", "Re4", "Re5", "Re6", "Re7", "Re8",
    "Qe1", "Qe2", "Qe3", "Qe4", "Qe5", "Qe6", "Qe7", "Qe8",
    "Ke1", "Ke2", "Ke3", "Ke4", "Ke5", "Ke6", "Ke7", "Ke8",

    "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8",
    "Nf1", "Nf2", "Nf3", "Nf4", "Nf5", "Nf6", "Nf7", "Nf8",
    "Bf1", "Bf2", "Bf3", "Bf4", "Bf5", "Bf6", "Bf7", "Bf8",
    "Rf1", "Rf2", "Rf3", "Rf4", "Rf5", "Rf6", "Rf7", "Rf8",
    "Qf1", "Qf2", "Qf3", "Qf4", "Qf5", "Qf6", "Qf7", "Qf8",
    "Kf1", "Kf2", "Kf3", "Kf4", "Kf5", "Kf6", "Kf7", "Kf8",

    "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8",
    "Ng1", "Ng2", "Ng3", "Ng4", "Ng5", "Ng6", "Ng7", "Ng8",
    "Bg1", "Bg2", "Bg3", "Bg4", "Bg5", "Bg6", "Bg7", "Bg8",
    "Rg1", "Rg2", "Rg3", "Rg4", "Rg5", "Rg6", "Rg7", "Rg8",
    "Qg1", "Qg2", "Qg3", "Qg4", "Qg5", "Qg6", "Qg7", "Qg8",
    "Kg1", "Kg2", "Kg3", "Kg4", "Kg5", "Kg6", "Kg7", "Kg8",

    "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8",
    "Nh1", "Nh2", "Nh3", "Nh4", "Nh5", "Nh6", "Nh7", "Nh8",
    "Bh1", "Bh2", "Bh3", "Bh4", "Bh5", "Bh6", "Bh7", "Bh8",
    "Rh1", "Rh2", "Rh3", "Rh4", "Rh5", "Rh6", "Rh7", "Rh8",
    "Qh1", "Qh2", "Qh3", "Qh4", "Qh5", "Qh6", "Qh7", "Qh8",
    "Kh1", "Kh2", "Kh3", "Kh4", "Kh5", "Kh6", "Kh7", "Kh8"]

board = chess.Board()
baseboard = chess.BaseBoard()

class MatchMove:
    id = 0
    move = None

#PGNフォーマットから座標に変換
#多分今使われていない？
def convertSquare(move):
    num1 = int(dict[move[0]])
    num2 = int(move[1])
    num3 = int(dict[move[2]])
    num4 = int(move[3])

    square = (9 - num2) * 8 - num1
    square2 = (9 - num4) * 8 - num3

    return square, square2, move[2]+move[3]

#リストをnumpy配列に変換する
def convertArray(tmp):   
    obs = []
    count = 0

    for line_str in tmp:
        for cha in line_str:
           
            if re.compile("[a-z]").search(cha):
                if cha == "p":
                    obs.append(1)
                  
                elif cha == "n":
                    obs.append(3)
                    
                elif cha == "b":
                    obs.append(4)
                  
                elif cha == "r":
                    obs.append(5)
                   
                elif cha == "q":
                    obs.append(9)
                   
                elif cha == "k":
                    obs.append(10)
                  

            elif re.compile("[A-Z]").search(cha):
                if cha == "P":
                    obs.append(-1)
        
                elif cha == "N":
                    obs.append(-3)
                 
                elif cha == "B":
                    obs.append(-4)
                   
                elif cha == "R":
                    obs.append(-5)
                   
                elif cha == "Q":
                    obs.append(-9)
                    
                elif cha == "K":
                    obs.append(-10)
                   

            elif re.compile("\d").search(cha):
                for i in range(int(cha)):
                    obs.append(0)
                    count += 1

                count -= 1    
        count += 1

    return obs    

#ランダムに動く時の関数
def random_move():
    print("random!")
    #rndnum = random.randint(0, MOVESTYPE_NUM)

    moves = []
    count = 0
    for i in board.legal_moves:
        moves.insert(count, i)
        count += 1
        #print(i, end=" ")

    rndnum = random.randint(0, count -1)
    output = board.san(moves[rndnum])
    print("output = " + str(output))

    matchList = []

    for i in range(MOVESTYPE_NUM):
        matchMove = MatchMove()
        moves_foot = str(movesType[i][-2] + movesType[i][-1])
        choice_foot = str(output[-2] + output[-1])

        if moves_foot == choice_foot:
            matchMove.id = i
            matchMove.move = movesType[i]
            matchList.append(matchMove)
            print("matching in random = " + matchMove.move)

    for j in range(len(matchList)):
        moves_head = str(matchList[j].move[0])
        choice_head = str(output[0])
        if moves_head == choice_head:
            print("return string = " + str(matchList[j].move))
            return matchList[j].id

    #output = str(moves[rndnum])     #outputはuci形式で
    #choiceSquare, square2, direction = convertSquare(output)        #移動元の座標を取得
    #print(str(choiceSquare))
    #choicePiece = str(board.piece_at(choiceSquare)).upper()  #移動元座標の駒を取得
    #print(choicePiece)

    #if str(choicePiece) == "P":
        #output = direction
    #else:
        #output = str(choicePiece) + direction

    #print("choice = " + str(output))


    #uci形式にしたlegal_movesの手をmovestypeから検索する、あてはまった番号を返す
    #for i in range(MOVESTYPE_NUM):
    #    tmp1 = str(output)
    #    tmp2 = str(movesType[i])

    #    if tmp1 == tmp2:
            #print("select :" + tmp1)
            #print("cnt: " + str(cnt))
    #        return i+1

    #return i+1    

#盤面のリセット
def reset():
    board.reset()
    tmp = re.compile("\w+/\w+/\w+/\w+/\w+/\w+/\w+/\w+").search(str(board.fen)).group(0).split("/")
    obs = convertArray(tmp)

    return np.array(obs)           

#ターンの処理
def step(action):

    #現時点での盤面情報を返り値obsに代入
    tmp = re.compile("\w+/\w+/\w+/\w+/\w+/\w+/\w+/\w+").search(str(board.fen)).group(0).split("/")
    obs = convertArray(tmp)
    board_before = np.array(obs)

    #legal_movesの情報を返り値infoに代入
    moves = []
    count = 0
    for i in board.legal_moves:
        moves.insert(count, i)
        count += 1

    info = board.legal_moves       

    #agentが選んだ手をmovesTypeリストから持ってくる
    output = str(movesType[action])
    print("select = " + output)
    matchList = []

    for move in board.legal_moves:
        legal = str(board.san(move))
        print("legal = " + legal)
        matchMove = MatchMove()
        choice_foot = str(output[-2] + output[-1])
        legal_foot = str(legal[-2] + legal[-1])

        if legal_foot == choice_foot:
            #matchMove.id = i
            #matchMove.move = legal
            matchList.append(legal)
            print("matching = " + legal)

    for j in range(len(matchList)):
        legal_head = str(matchList[j][0])
        choice_head = str(output[0])
        if legal_head == choice_head:
            select_move = str(board.parse_san(matchList[j]))

    #ここでlegal_movesからの検索処理
    #選んだ手をboard.parse_san()する
    #エラーが返ってこなければそれは打てる手、かつfrom_uciに使える形式に変換できる
    #san = None
    #try:
    #    san = str(board.parse_san(output))
    #except ValueError:
    #    #ゲームオーバー処理
    #    print("Illegal Move!!")
    #    r = -10
    #    done = True
    #    result_obs = np.array(obs)
    #    return(result_obs, r, done, info)

    #agentが選んだコマを動かす
    try:
        move = chess.Move.from_uci(select_move)
        board.push(move)
        print(board)
        print()

        #square, square2, hoge = convertSquare(str(move))
        #movedPiece = board.remove_piece_at(square)
        #board.set_piece_at(square2, movedPiece)

        #print(board)
        #print()

        #print("choice: " + str(move))
    except ValueError:
        #ゲームオーバー処理
        print("Illegal Move!!")
        r = -10
        done = True
        result_obs = np.array(obs)
        return(result_obs, r, done, info)

    #現時点での盤面情報を返り値obsに代入
    tmp = re.compile("\w+/\w+/\w+/\w+/\w+/\w+/\w+/\w+").search(str(board.fen)).group(0).split("/")
    obs = convertArray(tmp)
    board_after_agent = np.array(obs)

    #ゲームのクリア判定処理
    if board.is_checkmate():
        print("Agent checkmate!")
        r = 10
        done = True
        return(board_after_agent, r, done, info)

    elif board.is_stalemate():
        print("Draw(stalemate)")
        r = 0
        done = True
        return(board_after_agent, r, done, info)

    elif board.is_game_over():
        print("Draw(game over)")    
        r = 0
        done = True
        return(board_after_agent, r, done, info)

    else:
        sum1 = 0
        sum2 = 0
        for before in board_before:
            sum1 += before

        for after_agent in board_after_agent:
            sum2 += after_agent

        r = sum1 - sum2
        done = False

    #enemy turn
    #ゲームが終了していなければ処理を行う
    if not done:

        #敵はlegal_movesの中から手を選ぶ
        moves = []
        count = 0
        for i in board.legal_moves:
            moves.insert(count, i)
            count += 1

        rndnum = random.randint(0, count -1)
        output = str(moves[rndnum])
        convertSquare(output)

        #敵が選んだコマを動かす
        try:
            move = chess.Move.from_uci(output)
            board.push(move)
            print("enemy choice: " + str(move))

            #square, square2, hoge = convertSquare(str(move))
            #movedPiece = board.remove_piece_at(square)
            #board.set_piece_at(square2, movedPiece)

        except:
            print("except!!")
            print(output) 

        #現時点での盤面情報の代入
        tmp = re.compile("\w+/\w+/\w+/\w+/\w+/\w+/\w+/\w+").search(str(board.fen)).group(0).split("/")
        obs = convertArray(tmp)
        board_after_enemy = np.array(obs)

        #ゲームの終了判定
        if board.is_checkmate():
            print("Enemy checkmate!")
            r = -10
            done = True
            return(board_after_enemy, r, done, info)

        elif board.is_stalemate():
            print("Draw(stalemate)")
            r = 0
            done = True
            return(board_after_enemy, r, done, info)

        elif board.is_game_over():
            print("Draw(game over)")
            r = 0
            done  = True
            return(board_after_enemy, r, done, info)

        else:
            sum3 = 0
            for after_enemy in board_after_enemy:
                sum3 += after_enemy

            r = sum2 - sum3   
            done = False

        print(board)    


        #board情報を配列に変換
        #tmp = re.compile("\w+/\w+/\w+/\w+/\w+/\w+/\w+/\w+").search(str(board.fen)).group(0).split("/")
        #obs = convertArray(tmp)         

    #盤面配列はnumpy配列に変換する
    result_obs = np.array(obs)

    return(result_obs, r, done, info)


    #人操作用
    #if board.is_game_over():
    #    print("enemy win")
    #    break

    #print(board)

    #while True:
    #    try:
    #        myinput = input("input? > ")
    #        board.push_san(myinput)
    #        break
    #    except ValueError:
    #        pass
