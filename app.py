from flask import Flask, render_template
import game_of_life as g
app = Flask(__name__)



@app.route('/')
def home():
	g.GameOfLife(width=10, height=10)
	return render_template('index.html')

@app.route('/live')
def live():
	game = g.GameOfLife()
	if game.counter > 0:
		game.form_new_generation()
	game.counter = game.counter + 1
	game.form_new_generation()
	return render_template('live.html', life=game)


if __name__ == "__main__":
	app.run(debug=True)
