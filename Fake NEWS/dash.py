import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
from PIL import Image

file1=open('F:\\result.txt','r')
a=file1.read()
file1.close()
#Dash components
app = dash.Dash()
'''
image_filename = 'wc_1.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
'''
app.layout = html.Div(children=[
    html.H1(children='Fake News Detection and Analysis',style={'textAlign': 'center'}),
    html.Div(children=[
        html.P('Dash converts Python into our GUI for Presentation')
    ]),
    
    html.H2('Different Models Accuracies and Scores'),

    #For print of Accuracy
    html.Div(children=
            dcc.Textarea(
                    readOnly='True', 
                    #type='text',
                    value=a,
                    rows=15,
                    #value="The Accuracy and score of various algorithms is :\nNAIVE BAYES - %0.4f\nLOGISTIC REGRESSION - %0.4F\nRANDOM FOREST - %0.4\nEXTRA TREE CLASSIFIER - %0.4\nADA BOOST - %0.4\nXGBOOST - %0.4" %(acc_score_1,acc_score_2,acc_score_rfc,acc_score_etc,acc_score_3),
                    style={'width': '80%'}
            ),
            style={'textAlign': 'center'},
    ),
    #html.Div(children=
            html.H2('Data Analysis Graph'),
            dcc.Graph(
                id='graph',
                figure={
                    'data': [go.Bar(
                        x= l1,
                        y= l2,
                    )],
                    'layout': go.Layout (
                            title='Getting Real about Fake News',
                            xaxis= {'title': 'type'},
                            yaxis= {'title': 'count'}
                    )
                }
            ),
            dcc.Graph(
                id='graph1',
                figure={
                    'data': [go.Bar(
                        x= m1,
                        y= m2,
                    )],
                    'layout': go.Layout (
                            title='FAke Real',
                            xaxis= {'title': 'label'},
                            yaxis= {'title': 'count'}
                    )
                }
            ),
            dcc.Graph(
                id='graph2',
                figure={
                    'data': [go.Bar(
                        x= n1,
                        y= n2,
                    )],
                    'layout': go.Layout (
                            title='ISOT Fake News Dataset',
                            xaxis= {'title': 'label'},
                            yaxis= {'title': 'count'}
                    )
                }
            ),
            dcc.Graph(
                id='graph3',
                figure={
                    'data': [go.Bar(
                        x= o1,
                        y= o2,
                    )],
                    'layout': go.Layout (
                            title='fake_real_news_dataset-master',
                            xaxis= {'title': 'label'},
                            yaxis= {'title': 'count'}
                    )
                }
            ),
    #),
    #html.Div(children=
            html.H2('WordCloud'),            
            #init_notebook_mode(connected=True),
            #html.Img(src='F:\wc_1.png',)
            #html.Img(src='data:wc_1.png;base64,{}'.format(encoded_image))
            Image.open('F:\\wc_1.png').show()
    #)
    
])

#For Running the server
app.run_server()
