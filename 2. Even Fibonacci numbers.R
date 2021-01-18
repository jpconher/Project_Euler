# problem 2

start_time <- Sys.time()

# obtain Fibonacci sequence up to 4000000
fibonacci <- c(1,2)
while(fibonacci[length(fibonacci)] < 4000000){
  fibonacci <- c(fibonacci, sum(fibonacci[length(fibonacci)], fibonacci[length(fibonacci)-1]))
}

# sum even elements in fibonacci sequence
sum <- sum(fibonacci[fibonacci %% 2 == 0])

end_time <- Sys.time()
end_time - start_time