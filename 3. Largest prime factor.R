# Problem 3

start_time <- Sys.time()

number <- 600851475143

# get factors
factors <- vector()
if (number %% 2 == 0){ # we treat 2 as a separate case because it is the only even prime factor
  number <- number/2
  factors <- 2
  while(number %% 2 == 0){
    number <- number/2
  }
}

candidate <- 3
while(number > 1){
  if(number %% candidate == 0){
    number <- number/candidate
    factors <- c(factors, candidate)
    if(sum(candidate %% factors[factors <= sqrt(candidate)] == 0) == 0) largest_prime_factor <- candidate # all composite numbers have a factor <= sqrt(number)
    while(number %% candidate == 0){
      number <- number/candidate
    }
  }
  candidate <- candidate + 2
}

end_time <- Sys.time()
end_time - start_time
