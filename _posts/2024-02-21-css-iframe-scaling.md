---
layout: post
title: "CSS fun: scaling iframes"
---

It is a while since I refreshed my website so I thought I would experiment a
bit with <abbr title="Cascading Style Sheets">CSS</abbr> to explore my options
a bit.

I sometimes want to embed  a web page within another so that I can give a complementary
view of the content.
And I want to be able to resize the web page instead of having it a fixed size.
It is a bit tricky to do this in a way that works for all browsers: phones and tablets are tricky!

*[Note: After originally posting this page, I had to come back and add a whole other
section "The second attempt" becaues it did not work for touchscreens.
And, in the end, I am a bit frustrated with how much code I had to write to make this work.]*

## The first attempt

My first attempt comes pretty close. It works great on desktops and laptops but not on ipads.
But I will go through it in detail because it is mostly just standard CSS and HTML with just a small amount
of Javascript and because it is the starting point for the second (working) attempt.
(The part of this that will have to change is the use of "resize" in the final CSS.)

The ingredients of the first attempt are

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
        the_iframe.style.transform = `scale(${window_scale})`;
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
    <iframe id="the_iframe" src="../about/index.html" title="Blog title page"></iframe>
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

This approach has two problems.

1. It does not work on iOS (Safari or Chrome) because the resize handle does not show up.
2. Even on a laptop, it is not that great because the resize handle is at the bottom corner of the left-hand box.
   There is no way to move the handle so that dragging anywhere on the vertical divider resizes the box.

## The second attempt

The second attempt is based on two articles by [Phuoc Nguyen](https://phuoc.ng/)
that implement a similar interface by creating three boxes: a left-hand side,
a 2px-wide box that is used as a dragbar, and a right-hand side.
The [first article](https://phuoc.ng/collection/html-dom/create-resizable-split-views/) uses plain Javascript/typescript
while the [second article](https://phuoc.ng/collection/react-drag-drop/create-resizable-split-views/) uses React.

The important thing here is that, because we implement the dragbar ourselves, we have complete control over
its appearance and, critically, we can add support for [touch events](https://developer.mozilla.org/en-US/docs/Web/API/Touch_events)
to fix the problems on touchscreen devices.

- The HTML is similar to the first version except that, this time,
  we have an additional "div" that is used to implement the dragbar.

      <div class='splitter'>
        <div class='splitter__left'>
          Left
        </div>
        <div class='splitter__resizer' id='resizer'>
        </div>
        <div class='splitter__right' id='iframe_box2'>
          <iframe id="iframe2" src="../about/index.html" title="Blog title page"></iframe>
        </div>
      </div>

- The basics of the CSS support are basically the same as in the first attempt
  except that now we have to specify the style of the dragbar.
  It
  has an off-gray color,
  goes the full height,
  is two "pixels" wide,
  the cursor changes to a left-right arrow when it is over the dragbar,
  and both user selection and touch action are initially off.

      <style>
      .splitter__resizer {
          background-color: rgb(203 213 225);
          height: 100%;
          width: 2px;
          cursor: ew-resize;
          user-select: none;
          touch-action: none;
      }
      </style>

  (The reason I put quotations round "pixels" above is that, apparently,
  the "px" measurement used in CSS is [really an angular measurement](http://inamidst.com/stuff/notes/csspx).)

- The big difference between the two approaches is that we need to write quite a lot
  of Javascript because we have to implement all the dragbar behavior ourselves.

  - The entire block of code is only executed after all the HTML has been
    loaded - this makes the code less sensitive to whether the script is
    loaded in the page header or embedded somewhere in the page.

    Also, the first thing we do is extract all the key elements that
    we need to refer to.

        <script>
        document.addEventListener('DOMContentLoaded', function () {
            const resizer = document.getElementById('resizer');
            const container = resizer.parentNode;
            const leftSide = resizer.previousElementSibling;
            const rightSide = resizer.nextElementSibling;

            [...]
        });
        </script>

  - When the dragbar is moved, we need to adjust the width of the
    left-hand box. (This will be used for both mouse and touch events.)

            const updateWidth = (leftWidth, dx) => {
                const newLeftWidth = (leftWidth + dx);
                leftSide.style.width = `${newLeftWidth}px`;
            };

  - And we also have code to add and remove the cursor,
    user selection and pointer events.
    (This is explained in Phuoc Ng's original articles.)

           const updateCursor = () => {
               resizer.style.cursor = 'ew-resize';
               document.body.style.cursor = 'ew-resize';
               leftSide.style.userSelect = 'none';
               leftSide.style.pointerEvents = 'none';
               rightSide.style.userSelect = 'none';
               rightSide.style.pointerEvents = 'none';
           };

           const resetCursor = () => {
               resizer.style.removeProperty('cursor');
               document.body.style.removeProperty('cursor');
               leftSide.style.removeProperty('user-select');
               leftSide.style.removeProperty('pointer-events');
               rightSide.style.removeProperty('user-select');
               rightSide.style.removeProperty('pointer-events');
           };

  - With those helper functions in place, we can now define what
    is to happen on mouse-down, mouse-move and mouse-up events.

    On mouse-down, we record where the slider is and where the cursor is.
    On mouse-move, we call "updateWidth" to resize the left-hand box.
    (All the other boxes will be updated by the HTML layout engine.)
    On mouse-up, we stop tracking the mouse.

           const mouseDownHandler = function (e) {
               const startx = e.clientX;
               const leftWidth = leftSide.getBoundingClientRect().width;

               const mouseMoveHandler = function (e) {
                   updateWidth(leftWidth, e.clientX - startx);
                   updateCursor();
               };

               const mouseUpHandler = function () {
                   resetCursor();
                   document.removeEventListener('mousemove', mouseMoveHandler);
                   document.removeEventListener('mouseup', mouseUpHandler);
               };

               // Attach the listeners to document
               document.addEventListener('mousemove', mouseMoveHandler);
               document.addEventListener('mouseup', mouseUpHandler);
           };

           resizer.addEventListener('mousedown', mouseDownHandler);

  - Handling touch events is very similar except that we deal with
    the touchstart, touchmove and touchend events.

           const touchStartHandler = function (e) {
               const touch = e.touches[0];
               const startx = touch.clientX;
               const leftWidth = leftSide.getBoundingClientRect().width;

               const touchMoveHandler = function (e) {
                   const touch = e.touches[0];
                   updateWidth(leftWidth, touch.clientX - startx);
                   updateCursor();
               };

               const touchEndHandler = function () {
                   resetCursor();
                   document.removeEventListener('touchmove', mouseMoveHandler);
                   document.removeEventListener('touchend', mouseUpHandler);
               };

               // Attach the listeners to document
               document.addEventListener('touchmove', touchMoveHandler);
               document.addEventListener('touchend', touchEndHandler);
           };
           resizer.addEventListener('touchstart', touchStartHandler);

  - And, finally, we have the resize observer to rescale the iframe whenever
    the box containing it is resized.

           const resizeObserver2 = new ResizeObserver((entries) => {
               for (const entry of entries) {
                   const outer = entry.target;
                   const inner = outer.children[0];
                   const window_scale = outer.clientWidth / 800;
                   inner.style.transform = `scale(${window_scale})`;
                   inner.height = window.innerHeight / window_scale;
               }
           });
           resizeObserver2.observe(iframe_box2);

    (Incidentally, as I was debugging this, I was stuck for ages on why scaling
    was not working properly. It turns out that I was trying to rescale the
    iframe when the size of the iframe changed and this did not work because
    the iframe does not change size just because its parent box has changed size.
    Watching its parent box fixed this.)

With all that code in place, we finally have a resizable box --- you can drag the
dragbar between the two boxes and drag it from left to right and watch the
embedded web page scale itself to fit the available space.

<style>
.splitter {
display: flex;
height: 90vh;
border: 1px solid rgb(203 213 225);
}
.splitter__left {
min-width:200px;
align-items: center;
display: flex;
justify-content: center;
}
.splitter__resizer {
background-color: rgb(203 213 225);
height: 100%;
width: 2px;

cursor: ew-resize;
user-select: none;
touch-action: none;
}
.splitter__right {
flex: 3;

min-width:200px;
overflow: hidden;
}
#iframe2 {
width: 800px;
}
#iframe2 {
transform-origin: 0 0;
}
</style>

<div class='splitter'>
<div class='splitter__left'>
Left
</div>
<div class='splitter__resizer' id='resizer'>
</div>
<div class='splitter__right' id='iframe_box2'>
<iframe id="iframe2" src="../about/index.html" title="Blog title page"></iframe>
</div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function () {
// Query the element
const resizer = document.getElementById('resizer');
const container = resizer.parentNode;
const leftSide = resizer.previousElementSibling;
const rightSide = resizer.nextElementSibling;

const updateWidth = (leftWidth, dx) => {
    const newLeftWidth = (leftWidth + dx);
    leftSide.style.width = `${newLeftWidth}px`;
};

const updateCursor = () => {
    resizer.style.cursor = 'ew-resize';
    document.body.style.cursor = 'ew-resize';
    leftSide.style.userSelect = 'none';
    leftSide.style.pointerEvents = 'none';
    rightSide.style.userSelect = 'none';
    rightSide.style.pointerEvents = 'none';
};

const resetCursor = () => {
    resizer.style.removeProperty('cursor');
    document.body.style.removeProperty('cursor');
    leftSide.style.removeProperty('user-select');
    leftSide.style.removeProperty('pointer-events');
    rightSide.style.removeProperty('user-select');
    rightSide.style.removeProperty('pointer-events');
};

const mouseDownHandler = function (e) {
    const startx = e.clientX;
    const leftWidth = leftSide.getBoundingClientRect().width;

    const mouseMoveHandler = function (e) {
        updateWidth(leftWidth, e.clientX - startx);
        updateCursor();
    };

    const mouseUpHandler = function () {
        resetCursor();
        document.removeEventListener('mousemove', mouseMoveHandler);
        document.removeEventListener('mouseup', mouseUpHandler);
    };

    // Attach the listeners to document
    document.addEventListener('mousemove', mouseMoveHandler);
    document.addEventListener('mouseup', mouseUpHandler);
};

const touchStartHandler = function (e) {
    const touch = e.touches[0];
    const startx = touch.clientX;
    const leftWidth = leftSide.getBoundingClientRect().width;

    const touchMoveHandler = function (e) {
        const touch = e.touches[0];
        updateWidth(leftWidth, touch.clientX - startx);
        updateCursor();
    };

    const touchEndHandler = function () {
        resetCursor();
        document.removeEventListener('touchmove', mouseMoveHandler);
        document.removeEventListener('touchend', mouseUpHandler);
    };

    // Attach the listeners to document
    document.addEventListener('touchmove', touchMoveHandler);
    document.addEventListener('touchend', touchEndHandler);
};

resizer.addEventListener('mousedown', mouseDownHandler);
resizer.addEventListener('touchstart', touchStartHandler);

const resizeObserver2 = new ResizeObserver((entries) => {
    for (const entry of entries) {
        const outer = entry.target;
        const inner = outer.children[0];
        const window_scale = outer.clientWidth / 800;
        inner.style.transform = `scale(${window_scale})`;
        inner.height = window.innerHeight / window_scale;
    }
});

resizeObserver2.observe(iframe_box2);
});
</script>

So, now that I have something that works, what am I going to do with it?
To be honest, I am a bit disturbed by the complexity of the solution
and by the amount of code I left out that would have made the solution
more flexible and robust.
I suspect that the right solution would have been to find an existing
library and use that.
