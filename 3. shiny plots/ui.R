library(shiny)
library(DT)

shinyUI(fluidPage(
  

  titlePanel("Tarea Shiny App"),
  tabsetPanel(
    tabPanel("Shiny App", 
             plotOutput("scatter_plot",
                        click = 'clk',
                        dblclick = 'dclk',
                        hover = 'mhover',
                        brush = 'mbrush'),
             dataTableOutput("DT_mtcars")
    )
  )
  
  
))