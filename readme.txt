EVERYTHING DONE!!

just these 5 things to look into:
    a) client connection is not closed if u dont answer. rather if u ans after 60s, it says u took more than 60s n doesnt accept ur ans
    (we might have to change this)
    b) i made some changes and this program apparantly doesnt work for TOT_CLIENT_NO = 1 anymore
    (ig this is not an issue cos were gonna use at least 4 clients at once)
    c) the program randomly glitches at times but works most the time
    (idk if theres anything we can do abt that)
    d) if a client just exits without answering, other clients keep waiting at the end after answering the questions. no result is produced
    e) no validation for (TOT_CLIENT_NO + 1)th c
    
d,e are weird cases, c is ultra weird n we cant do anything. b is fine

i think we shud jus take care of a n were done