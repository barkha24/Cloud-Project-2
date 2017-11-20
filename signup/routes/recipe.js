var express = require( "express" );
var app = express();
var querystring = require("querystring");


app.get('/getRecipe', function(req, res){
var format = req.query.format,
recipeId=req.query.recipeId;

//set content of response
res.contentType('application/json');

//list of recipies
//var recipe = [{ title: 'cookie'},{ title: 'cake'}];
var recipe ={}
recipe.title= "cookie";

//JSON serialize for JSON representation of recipes
var recipeJSON= JSON.stringify(recipe);

res.send(recipeJSON);
});
app.get('/userInfo' , function(req,res){
var userId= req.query.userId;
//List of user information
var userInfo={}
userInfo.id="12345";
userInfo.name="Bob";

res.send(userInfo);


});
app.get('/getRecipes' , function(req,res){

var user= req.query.user;

//List of recipe information
var recipeInfo ={}
recipeInfo.id="123";
recipeInfo.name="cookie";
recipeInfo. ingredients="egg,flour,suger";
recipeInfo.prepTime= "20 min";
recipeInfo.description="blah blah";

var recipeInfoJSON = JSON.stringify(recipeInfo);
res.send(recipeInfoJSON);

});
app.get('/getRecipe' , function(req,res){

var format = req.query.format,
recipeId=req.query.recipeId,
getRecipe=req.params.getRecipe,
format=req.query.format;

});

app.listen(80);
