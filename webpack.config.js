var webpack = require('webpack');
var ExtractTextPlugin = require('extract-text-webpack-plugin'); //css单独打包
const UglifyJSPlugin = require('uglifyjs-webpack-plugin');

var plugins = [];
plugins.push(new ExtractTextPlugin('[name].css')); //css单独打包
plugins.push(new UglifyJSPlugin());

module.exports = {
    entry:[
        './app/app.js'
    ],
    output: {
        path: `${__dirname}/app/static`,
        filename: 'bundle.js',
    },
    module  :{
        loaders: [{
            test: /\.css$/,
            exclude: /^node_modules$/,
            use: ExtractTextPlugin.extract({
                fallback: "style-loader",
                use: [
                    {
                        loader:'css-loader',
                        options:{minimize: true}
                    }
                ]
            })
          }, {
            test: /\.less$/,
            exclude: /^node_modules$/,
            use: ExtractTextPlugin.extract({
                fallback: "style-loader",
                use: [{
                    loader:"css-loader",
                    options:{minimize: true}
                },{
                    loader:"less-loader",
                    options:{minimize: true}
                }]
            })            
          }],
    },
    plugins,
}