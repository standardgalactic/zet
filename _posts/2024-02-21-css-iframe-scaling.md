---
layout: post
title: "CSS fun: scaling iframes"
---

It is a while since I refreshed my website so I thought I would experiment a
bit with <abbr title="Cascading Style Sheets">CSS</abbr> to explore my options
a bit.

I sometimes want to embed  a web page within another so that I can give a complementary
view of the content. The ingredients of this are

- Use an iframe to embed the web page.

      <iframe id="the_iframe" src="../index.html" title="Blog title page"></iframe>

- Add some buttons to change the contents of the iframe.

      <button onclick="changeSrc('the_iframe', '../about/index.html')">Change to: About</button>
      <button onclick="changeSrc('the_iframe', '../css-iframe-scaling/')">Change to: This page</button>

  And a little Javascript

      <script>
      function changeSrc(id, src) {
          document.getElementById(id).src=src;
      }
      </script>

- Create a ["flexbox"](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Flexbox)
  with two children to hold the iframe and the commentary.

  The following is adapted from [randompast/resize.html](https://gist.github.com/randompast/e3d2fc4319a35858918f).

      <div class="compare">
        <div class='left'>
          <ul>
            <li>Thing1</li>
            <li>Thing2</li>
            <li>Thing3</li>
          </ul>
        </div>
        <div class='right' id='iframe_box'>
          <iframe id="the_iframe" src="../index.html" title="Blog title page"></iframe>
        </div>
      </div>

      <style>
      .compare {
        display: flex;
        height: 90vh;
      }
      .compare > .left {
        /*flex: 1; prevents resize!*/
        min-width:200px;
        border-style: solid;
        border-width: 1px;
        resize: horizontal;
        overflow: auto;
      }
      .compare > .right {
        min-width:200px;
        flex:3;
        border-style: solid;
        border-width: 1px;
        width: 100%;
        overflow: hidden;
      }
      #the_iframe {
          width: 800px;
      }
      </style>

  Some of the key parts of this are

  - The height of the compare class is "90vh" which means "90% of the height of the viewport".
  - The compare class has the property "display: flex;" to make it a flexbox and the right-hand box
    has the property "flex: 3" to make it 3 times wider than the other at the start.
  - The left-hand box has the property "resize: horizontal;" to add a resizing handle in the bottom right.
    This makes it possible to move the boundary between the left and right boxes.
  - There are some "min-width" properties to prevent either box getting too small.

- I was initially quite frustrated because the iframe never seemed to be the size it ought to be.
  It was too short and the size of the content didn't match the size of the box assigned to it.

  The solution was a little more Javascript to apply a scaling transformation to the iframe
  so that it always filled the box perfectly no matter what size you set the right-hand box to.

  This works by dynamically adding "transform: scale(X);" to the iframe's CSS (where "X" is
  the appropriate scaling size) whenever the iframe's container is resized.
  Because of the way that transforms work, we also need to set the origin of the transformation to (0,0).

      <script>
      const resizeObserver = new ResizeObserver((entries) => {
        const window_scale = iframe_box.clientWidth / 800;
        the_iframe.style.transform = `scale(${window_scale});`;
        the_iframe.height = window.innerHeight / window_scale;
      });

      resizeObserver.observe(iframe_box);
      </script>

      <style>
      #the_iframe {
          transform-origin: 0 0;
      }
      </style>

It took a bit of experimentation to come up with that but, I think it works reasonably well.
You can try resizing the box below here and you can select different web pages to view.

<style>
.compare {
  display: flex;
  height: 90vh;
}
.compare > .left {
  /*flex: 1; prevents resize!*/
  min-width:200px;
  border-style: solid;
  border-width: 1px;
  resize: horizontal;
  overflow: auto;
}
.compare > .right {
  min-width:200px;
  flex:3;
  border-style: solid;
  border-width: 1px;
  width: 100%;
  overflow: hidden;
}
#the_iframe {
    width: 800px;
}
#the_iframe {
    transform-origin: 0 0;
}
</style>

<button onclick="changeSrc('the_iframe', '../about/index.html')">Change to: About</button>
<button onclick="changeSrc('the_iframe', '../css-iframe-scaling/')">Change to: This page</button>

<div class="compare">
  <div class='left'>
    <ul>
      <li>Thing1</li>
      <li>Thing2</li>
      <li>Thing3</li>
    </ul>
  </div>
  <div class='right' id='iframe_box'>
    <iframe id="the_iframe" src="../index.html" title="Blog title page"></iframe>
  </div>
</div>

<script>
function changeSrc(id, src) {
    document.getElementById(id).src=src;
}
</script>

<script>
const resizeObserver = new ResizeObserver((entries) => {
  const window_scale = iframe_box.clientWidth / 800;
  the_iframe.style.transform = `scale(${window_scale})`;
  the_iframe.height = window.innerHeight / window_scale;
});

resizeObserver.observe(iframe_box);
</script>

