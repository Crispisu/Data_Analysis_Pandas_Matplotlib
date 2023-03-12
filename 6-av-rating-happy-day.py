import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc

data = pd.read_csv('/Users/crisd/Documents/Python Practice/Data Analysis and Visualizations with Pandas and Matplotlib/reviews.csv', parse_dates=['Timestamp'])
data['Weekday'] = data['Timestamp'].dt.strftime('%A')
data['Day Number'] = data['Timestamp'].dt.strftime('%w')
weekday_average = data.groupby(['Weekday', 'Day Number']).mean()
weekday_average = weekday_average.sort_values('Day Number')

chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Rating by Month'
    },
    subtitle: {
        text: 'According to the Data provided in the course'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Month - Year'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x}: {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating by Month',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text='Analysis of course reviews', classes='text-h3 text-center q-pa-md')
    p1 = jp.QDiv(a=wp, text='These graphs reppresent course review analysis')

    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.xAxis.categories = list(weekday_average.index.get_level_values(0))
    hc.options.series[0].data = list(weekday_average['Rating'])

    return wp

jp.justpy(app)