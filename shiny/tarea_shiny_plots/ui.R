
library(shiny)

shinyUI(fluidPage(

    titlePanel("Shiny Plots"),

               fluidRow(
                 column(6,
                   plotOutput("plot_click_options",
                              click = "clk",
                              dblclick = "dclk",
                              hover = "mouse_hover",
                              brush = "mouse_brush"),
                   verbatimTextOutput("click_data")
                 ),
                 column(6,
                   tableOutput("mtcars_tbl")
                 )
               )
))
