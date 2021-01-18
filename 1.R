# problem 1

start_time <- Sys.time()

candidates <- 1:999
sum <- sum(candidates[candidates %% 3 == 0 | candidates %% 5 == 0])

end_time <- Sys.time()
end_time - start_time

