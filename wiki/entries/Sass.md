# CSS with Superpowers

## Install on Mac OS X or Linux (Homebrew)

If you use [the Homebrew package manager](https://brew.sh/) for Mac OS X or Linux, you can install Dart Sass by running

```bash
brew install sass/sass/sass
```

Run `sass --version` to be sure it installed correctly.


## [Sass Basics](https://sass-lang.com/guide/)

When you install Sass on the command line, you’ll be able to run the `sass` executable to compile `.sass` and `.scss` files to `.css` files. For example:

```bash
sass ./stylesheets/index.scss build/stylesheets/index.css
```
You can also watch individual files or directories with the `--watch` flag. The watch flag tells Sass to watch your source files for changes, and re-compile CSS each time you save your Sass. If you wanted to watch (instead of manually build) your `input.scss` file, you’d just add the watch flag to your command, like so:

```bash
sass --watch input.scss output.css
```


#### [Variables](https://sass-lang.com/guide/#variables)

Sass uses the `$` symbol to make something a variable. Here’s an example:

```scss
$font-stack: Helvetica, sans-serif;
$primary-color: #333;

body {
  font: 100% $font-stack;
  color: $primary-color;
}
```

```css
body {
  font: 100% Helvetica, sans-serif;
  color: #333;
}
```

When the Sass is processed, it takes the variables we define for the `$font-stack` and `$primary-color` and outputs normal CSS with our variable values placed in the CSS. This can be extremely powerful when working with brand colors and keeping them consistent throughout the site.