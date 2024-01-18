from flask import Flask, render_template, request, jsonify
import random
import urllib.request

app = Flask(__name__)

bird_names = ["Sparrow", "Robin", "Eagle", "Owl", "Penguin", "Flamingo", "Peacock", "Parrot"]

user_score = 0

@app.route('/')
def index():
    global user_score
    bird_name, bird_image_url = get_random_bird()
    return render_template('index.html', bird_name=bird_name, bird_image_url=bird_image_url, user_score=user_score)

@app.route('/check_answer', methods=['POST'])
def check_answer():
    global user_score
    selected_bird = request.form['selected_bird']
    correct_bird = request.form['correct_bird']

    if selected_bird == correct_bird:
        user_score += 1
        result = {'correct': True, 'score': user_score}
    else:
        user_score = max(0, user_score - 1)
        result = {'correct': False, 'score': user_score, 'correct_bird': correct_bird}

    bird_name, bird_image_url = get_random_bird()
    result['bird_name'] = bird_name
    result['bird_image_url'] = bird_image_url

    return jsonify(result)

def get_random_bird():
    bird_name = random.choice(bird_names)
    bird_image_url = f'https://picsum.photos/300/200?random={random.randint(1, 100)}'

    # You can use urllib to fetch the image and save it locally if needed
    urllib.request.urlretrieve(bird_image_url, "assets/black-throated-finch.jpeg")

    return bird_name, "assets/black-throated-finch.jpeg"

if __name__ == '__main__':
    print('hi')
    app.run(debug=True)
