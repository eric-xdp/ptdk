// https://github.com/michael-ciniawsky/postcss-load-config

module.exports = {
  plugins: {
    "postcss-import": {},
    "postcss-url": {},
    // to edit target browsers: use "browserslist" field in package.json
    "autoprefixer": {},
    'postcss-pxtorem': {
        rootValue ({ file }) {
          // file => 要编译的样式的路径
          return file.includes('vant') ? 37.5 : 75
        },
    // * 号代表把所有的属性 px 转 rem
        propList: ['*']
  },
}
}