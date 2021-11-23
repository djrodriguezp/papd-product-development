

library(shiny)

current_df <- NULL
clicked <- FALSE

shinyServer(function(input, output) {

    output$plot_click_options <- renderPlot({
      filtered_df<-NULL
      plot <- ggplot(mtcars, aes(wt, mpg)) + geom_point() 
              
      if(!is.null(input$mouse_brush)){
        filtered_df <- brushedPoints(mtcars, input$mouse_brush, xvar="wt", yvar="mpg")
      } else if(clicked && !is.null(current_df)){
        filtered_df <- current_df
      }
      
      if(!is.null(input$mouse_hover)){
        hover_df <- nearPoints(mtcars, input$mouse_hover, xvar="wt", yvar="mpg")
        plot <- plot  +  geom_point(data=hover_df, colour= "gray", size=6)
      }
      
      if(!is.null(filtered_df)){
        plot <- plot  +  geom_point(data=filtered_df, colour= "green")
      }
      plot
    })
    
    
    output$click_data <- renderPrint({
      rbind(c( input$clk$x, input$clk$y),  
      c( input$dclk$x, input$dclk$y),
      c(input$mouse_hover$x, input$mouse_hover$y),
      c(input$mouse_brush$xmin, input$mouse_brush$ymin),
      c(input$mouse_brush$xmax, input$mouse_brush$ymax))  
    })
    
    output$mtcars_tbl <- renderTable({
      
      if(!is.null(input$clk)){
        current_df <<- nearPoints(mtcars, input$clk, xvar="wt", yvar="mpg")
        clicked <<- TRUE
      }
      if(!is.null(input$mouse_brush)){
        current_df <- brushedPoints(mtcars, input$mouse_brush, xvar="wt", yvar="mpg")
        clicked <<- FALSE
      }
      #else if(!is.null(input$clk))
      #  df <- nearPoints(mtcars, input$clk, xvar="wt", yvar="mpg")
      else if(is.null(current_df) || !is.null(input$dclk)) {
        current_df <<- mtcars
        clicked <<- FALSE
      }
      
      current_df
    })
})
