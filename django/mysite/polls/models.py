from django.db import models

#import dependencies
import pandas as pd
import os
import matplotlib
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile
import plotly.tools as tls
tls.embed('https://plot.ly/~cufflinks/8')
import plotly.plotly as py
import cufflinks as cf
import plotly
from plotly.offline import init_notebook_mode, download_plotlyjs, plot, iplot
import plotly.offline as opy
import plotly.graph_objs as go
from django.views.generic import TemplateView


plotly.tools.set_credentials_file(username='SuperSue', api_key='cpPnfuLvDxRJv4YCMs8b')


plotly.offline.init_notebook_mode(connected=True)


cf.go_offline()



# Create your models here.




class Graph(TemplateView):
	def __init__(self,SheetName):

		self.bcg_data = pd.read_excel('immunization_data.xlsx', sheet_name=SheetName)
		self.template_name = 'Templates/graph.html'
		self.graph_data = SheetName

	def get_context_data(self, country = 'Afghanistan',**kwargs):
		context = super(Graph, self).get_context_data(**kwargs)

		
		
		x_axis_bcg = (list(self.bcg_data)[4:])

		bcg_data_plot = self.bcg_data[['country','2017','2016','2015','2014','2013','2012','2011','2010','2009','2008','2007','2006',
                 '2005','2004','2003', '2002', '2001', '2000','1999','1998','1997','1996','1995','1994','1993','1992','1991','1990', '1989','1988','1987', '1986',
                 '1985','1984', '1983','1982','1981','1980']]


		bcg_plot = bcg_data_plot.set_index('country')
		data = [
			go.Scatter(
			x= x_axis_bcg, 
			y=bcg_plot.loc[country]
			)
				]

		layout = go.Layout(
		title= self.graph_data +" Immunization",
		yaxis=dict(title='% Immunization'),
		xaxis=dict(title='Year')
		)

		fig = go.Figure(data=data, layout=layout)




		
		div = opy.plot(fig, auto_open=False, output_type='div')

		context['graph'] = div

		return context


	def getCountryList(self):
		country_list= self.bcg_data['country'].tolist()

		div = "<div><select id ='country' onChange = 'GetCountry();'>"
		
		for country in country_list:
			div = div + "<option>" + country + "</option>"
		div = div + "</select></div>"

		return div

		
		
		
