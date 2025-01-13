from flask import (Flask, render_template)

import os

app = Flask(__name__)

@app.route('/')
def welcomepage():
    return render_template('index.html')

#============= LINES CHARTS =====================================================
@app.route('/line-basic-v1')
def line_basic_v1():
    return render_template('/line/line-basic-v1.html')

@app.route('/line-basic-v2')
def line_basic_v2():
    return render_template('/line/line-basic-v2.html')

@app.route('/line-basic-v3-line-dots')
def line_basic_v3():
    return render_template('/line/line-basic-v3-line-dots.html')

@app.route('/line-basic-v4-line-dots-grid')
def line_basic_v4():
    return render_template('/line/line-basic-v4-line-dots-grid.html')

@app.route('/line-basic-v5-line-dots-grid-toolpit')
def line_basic_v5():
    return render_template('/line/line-basic-v5-line-dots-grid-toolpit.html')

@app.route('/line-basic-v6-line-dots-grid-zoom')
def line_basic_v6():
    return render_template('/line/line-basic-v6-line-dots-grid-zoom.html')

@app.route('/line-basic-v7-line-dots-grid-zoom-toolpit')
def line_basic_v7():
    return render_template('/line/line-basic-v7-line-dots-grid-zoom-toolpit.html')

@app.route('/line-basic-v8-time')
def line_basic_v8():
    return render_template('/line/line-basic-v8-time.html')

@app.route('/line-basic-v9-time')
def line_basic_v9():
    return render_template('/line/line-basic-v9-time.html')

@app.route('/line-basic-v10-time')
def line_basic_v10():
    return render_template('/line/line-basic-v10-time.html')


@app.route('/line-interactive-v1')
def interactive_line_v1():
    return render_template('/line/line-interactive-v1.html')

@app.route('/line-interactive-v2')
def interactive_line_v2():
    return render_template('/line/line-interactive-v2.html')

@app.route('/line-interactive-v3')
def interactive_line_v3():
    return render_template('/line/line-interactive-v3.html')

@app.route('/line-interactive-v4')
def interactive_line_v4():
    return render_template('/line/line-interactive-v4.html')


#============= BRUSH =====================================================
@app.route('/brush-v1')
def line_brush_v1():
    return render_template('/brush/brush-v1.html')

@app.route('/brush-v2')
def line_brush_v2():
    return render_template('/brush/brush-v2.html')

@app.route('/brush-v3')
def line_brush_v3():
    return render_template('/brush/brush-v3.html')

@app.route('/brush-v4')
def line_brush_v4():
    return render_template('/brush/brush-v4.html')

@app.route('/brush-v5')
def line_brush_v5():
    return render_template('/brush/brush-v5.html')

@app.route('/brush-v6')
def line_brush_v6():
    return render_template('/brush/brush-v6.html')

@app.route('/brush-v7')
def line_brush_v7():
    return render_template('/brush/brush-v7.html')

@app.route('/brush-v8')
def line_brush_v8():
    return render_template('/brush/brush-v8.html')

if __name__ == '__main__':
    app.run(debug=True)