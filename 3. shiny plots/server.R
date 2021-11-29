library(shiny)
library(ggplot2)
library(dplyr)
library(DT)

#Variables "Globales" para el manejor de los eventos
out_click <- NULL
out_brush <- NULL
out_hover <- NULL
out_df <- mtcars



shinyServer(function(input, output) {
 
  #Reactive para la definición de puntos según eventos 
  puntos <- reactive({
    #Click
    if(!is.null(input$clk$x)){
      df <- nearPoints(mtcars,input$clk,xvar='wt',yvar='mpg')
      out_click <<- rbind(out_click,df) %>% distinct()
      out_df <<- df
    }
    #Hover
    if(!is.null(input$mhover$x)){
      df <- nearPoints(mtcars,input$mhover,xvar='wt',yvar='mpg')
      out_hover <<- df
    }
    #Doble Click
    if(!is.null(input$dclk$x)){
      df <- nearPoints(mtcars,input$dclk,xvar='wt',yvar='mpg')
      out_click <<- setdiff(out_click,df)
      out_brush <<- setdiff(out_brush,df)
    }
    #Brush
    if(!is.null(input$mbrush)){
      df<-brushedPoints(mtcars,input$mbrush,xvar='wt',yvar='mpg')
      out_brush <<- rbind(out_brush,df) %>% distinct()
      out_df <<- df
    }
    
  })
  
  # Reactive para plotear gráfica con base a los puntos out_df
  scatter_plot <- reactive({
    plot(mtcars$wt,mtcars$mpg,xlab="wt",ylab="mpg", cex=2)
    puntos <-puntos()
    #Hover
    if(!is.null(out_hover)){
      points(out_hover[,'wt'],
             out_hover[,'mpg'],
             col = 'gray',
             pch = 16,
             cex = 2)}
    #Click
    if(!is.null(out_click)){
      points(out_click[,'wt'],
             out_click[,'mpg'],
             col = 'green',
             pch = 16,
             cex= 2)}
    #Brush
    if(!is.null(out_brush)){
      points(out_brush[,'wt'],
             out_brush[,'mpg'],
             col = 'green',
             pch = 16,
             cex = 2)}
  })
  
  #Enviando plot al UI
  output$scatter_plot = renderPlot({
    scatter_plot()
    
  })
  
  #Reactiva para DT
  DTtable <- reactive({
    input$clk
    input$dclk
    input$mbrush
    if((!is.null(out_brush)&!is.null(out_click))) {
      out_df <<- rbind(out_brush,out_click)
    }
    out_df 
  })
  
  #Enviado DT a la UI
  output$DT_mtcars = renderDataTable({
    DTtable() %>% datatable()
  })
  
})