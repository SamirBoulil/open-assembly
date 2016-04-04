var HtmlWebpackPlugin = require('html-webpack-plugin')
var ExtractTextPlugin = require("extract-text-webpack-plugin");
var HTMLWebpackPluginConfig = new HtmlWebpackPlugin({
  template: __dirname + '/app/index.html',
  filename: 'index.html',
  inject: 'body'
});

var DIST_DIR = __dirname + '/dist';

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
      {test: /\.js$/, exclude: /node_modules/, loader: "babel-loader"},
      // {
      //   test: /\.scss$/,
      //   loaders: ExtractTextPlugin.extract('css!sass')
      // }
    ]
  },
  sassLoader: {
    includePaths: ['node_modules/compass-mixins/lib']
  },
  plugins: [
    HTMLWebpackPluginConfig,
    new ExtractTextPlugin("style.css")
  ]
};
