# KeyBuddy

Check out a live version of KeyBuddy here:
`<link  to keyBuddy here>`


KeyBuddy, is similar to the chordie app, but I wouldn't call it a clone.
KeyBuddy was built as a companion app for anyone taking piano lessons.Its designed to be used as a supplemental learning tool, and NOT to replace traditional lessons.
The Backend if KeyBuddy is built on Flask with a PostgreSQL database. Frontend rendering is handled with React.

## Features & Implementation

### design and purpose

KeyBuddy is an SRS application (space repetition studier), it is designed to ask you a series of questions in a row, and time you your answers, if you answer fast, it will assume you have a handle on the question, and will not ask it in the series, if the opposite is true, it will ask you the question again until  yo have satisfied the timing requirements.  thats to say until you can answer within a couple of seconds of the question asked.
Using WebMid.js `https://webmidijs.org/api/`  and Tonal.js   `https://github.com/tonaljs/tonal`  KeyBuddy, will test you on chords, scales, key signatures and chord progressions


### Single-page-App

*React router and components*

KeyBuddy is a single page app. All “pages” are rendered at a root url “/” by a
collection of shuffling react components. The React router handles the logic
associated with component navigation and updates an addendum to the root route.
Re-rendering of child components is done through the React API.


Frontend and Backend Interaction*

[soon]

###Authentication

[soon]


# CRUDS


There are 6 main Models of this application,  users, lessons, published,reviews, courses, and details. Of these 6, the most important are lessons, courses, published and details.

lessons, lessons contains fields for type(of lesson), style, and key. The type of lesson would either be a 'scales' test,  a 'key' test, or a 'chord/chord progression' test, The user will be able to select the style of music, these notes are on like 'jazz' for instance. each lesson links to a details table where more information is revealed about the lesson such as : popular songs, chords and progressions in that particular key, as well as what that Key pulls to and pulls from note wise. This is all music theory.
The courses will be a user curated collection of 1-4 lessons. The user can use these courses to go through an intensified Space Repetition studying session.
In addition to that the user will also be able to publish, any curated courses, as well as use any other user curated courses. this way both users who are not as skilled, can mimic the more skilled players in their study sessions.
