from flask import Flask, render_template_string, request

app = Flask(__name__)

teams = {
    "CSK": {"name": "Chennai Super Kings", "score": 0, "wickets": 0, "overs": 0},
    "MI": {"name": "Mumbai Indians", "score": 0, "wickets": 0, "overs": 0},
    "RCB": {"name": "Royal Challengers Bangalore", "score": 0, "wickets": 0, "overs": 0},
    "KKR": {"name": "Kolkata Knight Riders", "score": 0, "wickets": 0, "overs": 0},
}

HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>IPL Score Tracker 🏏</title>
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <style>
        body { background:#1a1a2e; color:white; font-family:Arial; text-align:center; padding:20px; }
        h1 { color:#FFD700; }
        .team-card { background:#16213e; border:2px solid #FFD700; border-radius:15px; padding:20px; margin:15px auto; max-width:400px; }
        .score { font-size:2.5em; font-weight:bold; color:#FFD700; }
        .btn { background:#FFD700; color:black; border:none; padding:10px 20px; border-radius:10px; font-size:1em; cursor:pointer; margin:5px; }
        input { padding:8px; border-radius:8px; border:none; font-size:1em; width:60px; text-align:center; }
    </style>
</head>
<body>
    <h1>🏏 IPL Score Tracker</h1>
    {% for code, team in teams.items() %}
    <div class="team-card">
        <h2>{{ team.name }}</h2>
        <div class="score">{{ team.score }}/{{ team.wickets }}</div>
        <div>Overs: {{ team.overs }}</div>
        <form method="POST" action="/update/{{ code }}">
            <input type="number" name="runs" placeholder="Runs" min="0">
            <input type="number" name="wickets" placeholder="W" min="0" max="10">
            <input type="number" name="overs" placeholder="Ov" min="0" max="20">
            <br><br>
            <button type="submit" class="btn">Update Score</button>
        </form>
    </div>
    {% endfor %}
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML, teams=teams)

@app.route('/update/<team_code>', methods=['POST'])
def update(team_code):
    if team_code in teams:
        teams[team_code]['score'] = int(request.form.get('runs', 0))
        teams[team_code]['wickets'] = int(request.form.get('wickets', 0))
        teams[team_code]['overs'] = float(request.form.get('overs', 0))
    return index()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
