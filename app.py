from boggle import Boggle
from flask import Flask, request, render_template, jsonify, session

app = Flask(__name__)
app.config['SECRET KEY'] = "sdfgdsfgfdhggfh"

boggle_game = Boggle()


@app.route("/")
def show_homepage():
    """Show board"""

    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get("highscore", 0)
    number_plays = session.get("numberplays", 0)

    return render_template('index.html', board = board, highscore = highscore, number_plays = number_plays)

@app.route("/check-word")
def check_word():
    """Check if the word is in the dictionary"""

    word = request.args["word"]
    board = session['board']
    response = boggle_game.check_valid_word(board, word)

    return jsonify({'result': response})

@app.route('/post-score', methods=['POST'])
def post_score():
    """Receive scores, update the number of plays, update the high score is necessary"""

    score = request.json['score']
    highscore = session.get('highscore', 0)
    number_plays = session.get("numberplays", 0)

    session["numberplays"] = number_plays + 1
    session['highscore'] = max(score, highscore)

    return jsonify(brokeRecord = score > highscore)



