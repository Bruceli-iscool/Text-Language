//; A simple game for guessing animals
//; store answer
;let>answer=0
Welcome to animal guess! 
What is a animal that has a trunk?
//; use no answer message
;prompt> :answer
;if>{answer}==elephant|Yah! you are correct!
;if>{answer}!=elephant|wrong
//; use word blob
What animal is very fast?
;prompt> :answer
;if>{answer}==cheeta|Yah, You got it right
;if>{answer}!=cheeta|wrong

You completed the quiz!