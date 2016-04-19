var HtmlWebpackPlugin = require('html-webpack-plugin')
var ExtractTextPlugin = require("extract-text-webpack-plugin");

var DIST_DIR = __dirname + '/dist';

var HTMLWebpackPluginConfig = new HtmlWebpackPlugin({
  template: __dirname + '/app/index.html',
  filename: 'index.html',
  inject: 'body'
});
var ExtractTextPluginConfig =  new ExtractTextPlugin(__dirname + '/styles/style.css', {
  allChunks: true
});

module.exports = {
  entry: [
    './app/index.js'
  ],
  output: {
    path: DIST_DIR,
    filename: "index_bundle.js"
  },
  module: {
    loaders: [
      { test: /\.js$/, exclude: /node_modules/, loader: "babel-loader" },
      { test: /\.scss$/, loader: ExtractTextPlugin.extract('css!sass?indentedSyntax=true&sourceMap=true') },
      { test: /\.jpe?g$|\.gif$|\.png$|\.svg$|\.woff$|\.ttf$/, loader: "file" },
      {test: /\.woff$/, loader: "url-loader?limit=10000&mimetype=application/font-woff&name=[path][name].[ext]"},
      {test: /\.woff2$/, loader: "url-loader?limit=10000&mimetype=application/font-woff2&name=[path][name].[ext]"},
      {test: /\.(jpe?g|png|gif|woff2?|ttf|eot|svg)$/, loader: "file"}
    ]
  },
  sassLoader: {
    includePaths: ['node_modules/compass-mixins/lib']
  },
  plugins: [
    HTMLWebpackPluginConfig,
    ExtractTextPluginConfig
  ]
};
