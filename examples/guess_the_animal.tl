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
;if>{answer}==cheetah|Yah, You got it right
;if>{answer}!=cheetah|wrong
What animal is smart?
;prompt> :answer
;if>{answer}==monkey|Yah, You got it right
;if>{answer}==bruce|Yah, You got it right
;if>{answer}!=monkey|wrong
You completed the quiz!