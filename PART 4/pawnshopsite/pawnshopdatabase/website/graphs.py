import plotly.graph_objects as go
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.palettes import Category20c

import pandas as pd


def create_bar_chart(data):
    # Перетворюємо дані на списки x та y
    x_values = [entry['item_id'] for entry in data]
    y_values = [entry['total_sales'] for entry in data]

    fig = go.Figure([go.Bar(x=x_values, y=y_values)])
    fig.update_layout(title='Продажі за категоріями', xaxis_title='Категорії', yaxis_title='Продажі')
    return fig

def create_line_chart(data):
    x_values = [entry['month'] for entry in data]
    y_values = [entry['total_sales'] for entry in data]

    fig = go.Figure([go.Scatter(x=x_values, y=y_values, mode='lines', name='Лінія')])
    fig.update_layout(title='Лінійний графік', xaxis_title='Час', yaxis_title='Продажі')
    return fig

def create_pie_chart(data):
    labels = [entry['item_id'] for entry in data]
    values = [entry['total_sales'] for entry in data]

    fig = go.Figure([go.Pie(labels=labels, values=values)])
    fig.update_layout(title='Кругова діаграма продажів за категоріями')
    return fig

# Функція для створення стовпчикової діаграми Bokeh
from bokeh.embed import components

def create_bar_chart_bokeh(data):
    # Перетворюємо значення на float
    x_values = [str(entry['item_id']) for entry in data]  # Перетворюємо item_id на рядки
    y_values = [float(entry['total_sales']) for entry in data]  # Перетворюємо total_sales на float

    p = figure(x_range=x_values, title="Стовпчикова діаграма", toolbar_location=None, tools="")
    p.vbar(x=x_values, top=y_values, width=0.9)
    p.xaxis.axis_label = "Категорії"
    p.yaxis.axis_label = "Продажі"
    p.grid.grid_line_color = "white"

    script, div = components(p)  # Повертаємо script та div
    return script, div


# Функція для створення лінійного графіка Bokeh
def create_line_chart_bokeh(data):
    # Перетворюємо дані на списки x та y
    x_values = [entry['month'] for entry in data]
    y_values = [entry['total_sales'] for entry in data]

    p = figure(title="Лінійний графік", x_axis_label="Час", y_axis_label="Продажі", tools="pan,box_zoom,reset")
    p.line(x_values, y_values, legend_label="Лінія", line_width=2)
    return components(p)

# Функція для створення кругової діаграми Bokeh
def create_pie_chart_bokeh(data):
    # Перевірка структури даних
    print("Data for Pie Chart:", data)  # Додаємо виведення для дебагу

    # Перетворення списку словників у DataFrame
    df = pd.DataFrame(data)

    # Перевірка, чи містить DataFrame колонку 'item_id'
    if 'item_id' not in df.columns:
        print("Columns in the DataFrame:", df.columns)
        raise KeyError("'item_id' not found in the data")

    # Розрахунок кута для кожного сектора
    df['angle'] = df['total_sales'] / df['total_sales'].sum() * 2 * 3.14159  # Використовуємо pi

    # Встановлюємо кольори
    df['color'] = ['red'] * len(df)  # Replace 'some_value' with the actual value you want for the color

    # Створення графіка
    from bokeh.plotting import figure
    from bokeh.palettes import Category20c
    from bokeh.transform import cumsum

    p = figure(title="Кругова діаграма", toolbar_location=None, tools="hover", tooltips="@item_id: @total_sales", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='item_id', source=df)

    p.axis.visible = False
    p.grid.visible = False
    return components(p)


