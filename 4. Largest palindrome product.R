# Problem 4

library(stringr)

start_time <- Sys.time()

#store candidates
candidates <- sort(unique(as.vector(t(101:999%*%t(101:999)))), decreasing = T) #100 is ruled out as 100*XXX will start with X and end with a 0
candidate <- 0

i <- 1

while (candidate == 0) {
  candidate <- candidates[i]
  size_candidate <- str_length(candidate)
  for (k in 1:trunc(size_candidate/2)){
    if (substr(candidate, k, k) != substr(candidate, size_candidate+1-k, size_candidate+1-k)){
      candidate <- 0
      break
    }
  }
  i <- i + 1
}

#print largest palindrome
print(candidates[i-1])

end_time <- Sys.time()
end_time - start_time