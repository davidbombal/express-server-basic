# Very Basic Express Server with a Resource for Logging Keystrokes

## This code DOES NOT promote or encourage any illegal activities! The content in this document is provided solely for educational purposes and to create awareness!

## This is a proof of concept and could be improved on in a lot of ways.

1. To run this code use `git clone https://github.com/davidbombal/express-server-basic.git`
2. Run the command `cd/express-server-keylogger-basic`
3. Run the command `python3 setup.py`. This will do the basic setup on the Ubuntu server. It will install NodeJS, Node Package Manager (NPM) and also install all the modules required such as the Express web framework, the body-parser middleware used by Express.
4. Run the command `node server.js` to start the server on port ***8080***

You can use the GET and POST methods on the "/" endpoint.
- GET will show the keylogger data written to the server, with every page refresh.
- POST will write the data with the body
  `{
      keyboardData: <what user entered>
   }`
   
This is a little bare bones project that shows with little effort how powerful a few lines of server side JavaScript using Node can be. It can be improved with the addition of a database such as MongoDB paired with a module such as Mongoose (To validate and structure API input). Also, the addition of update, and remove operations would be quite easy to implement. I also didn't implement good exception handling for this project.   
