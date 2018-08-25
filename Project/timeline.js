
  var container = document.getElementById('visualization');

  // note that months are zero-based in the JavaScript Date object
  var items = new vis.DataSet([
    {id: 'A', content: 'Recession', start: '2007-12-31', end: '2009-06-01', type: 'background'},

    {start: new Date(2008,1,22),  content: 'Housing Bubble Pops'},
    {start: new Date(2009,1,9),  content: '2 million jobs lost in the last 4 months'},
    {start: new Date(2008,3,18), content: 'Fed Begins Bailouts'},
    // {start: new Date(1940,7,13), content: 'Battle of Britain - RAF vs. Luftwaffe'},
    // {start: new Date(1941,1,14), content: 'German Afrika Korps arrives in North Africa'},
    // {start: new Date(1941,5,22), content: 'Third Reich Invades the USSR'},
    // {start: new Date(1941,11,7), content: 'Japanese Attack Pearl Harbor'},
    // {start: new Date(1942,5,4),  content: 'Battle of Midway in the Pacific'},
    // {start: new Date(1942,10,8), content: 'Americans open Second Front in North Africa'},
    // {start: new Date(1942,10,19),content: 'Battle of Stalingrad in Russia'},
    // {start: new Date(1943,6,5),  content: 'Battle of Kursk - Last German Offensive on Eastern Front'},
    // {start: new Date(1943,6,10), content: 'Anglo-American Landings in Sicily'},
    // {start: new Date(1944,2,8),  content: 'Japanese Attack British India'},
    // {start: new Date(1944,5,6),  content: 'D-Day - Allied Invasion of Normandy'},
    // {start: new Date(1944,5,22), content: 'Destruction of Army Group Center in Byelorussia'},
    // {start: new Date(1944,7,1),  content: 'The Warsaw Uprising in Occupied Poland'},
    // {start: new Date(1944,9,20), content: 'American Liberation of the Philippines'},
    // {start: new Date(1944,11,16),content: 'Battle of the Bulge in the Ardennes'},
    // {start: new Date(1944,1,19), content: 'American Landings on Iwo Jima'},
    // {start: new Date(1945,3,1),  content: 'US Invasion of Okinawa'},
    // {start: new Date(1945,3,16), content: 'Battle of Berlin - End of the Third Reich'}
  ]);

  var options = {
    // Set global item type. Type can also be specified for items individually
    // Available types: 'box' (default), 'point', 'range'
    start: '2007-01-10',
    end: '2010-02-10',
    editable: false,
    type: 'point',
    showMajorLabels: false,
    // autoResize: true
  };

  var timeline = new vis.Timeline(container, items, options);

    /**
     * Move the timeline a given percentage to left or right
     * @param {Number} percentage   For example 0.1 (left) or -0.1 (right)
     */
    function move (percentage) {
        var range = timeline.getWindow();
        var interval = range.end - range.start;

        timeline.setWindow({
            start: range.start.valueOf() - interval * percentage,
            end:   range.end.valueOf()   - interval * percentage
        });
    }

    // attach events to the navigation buttons
    document.getElementById('zoomIn').onclick    = function () { timeline.zoomIn( 0.2); };
    document.getElementById('zoomOut').onclick   = function () { timeline.zoomOut( 0.2); };
    document.getElementById('moveLeft').onclick  = function () { move( 0.2); };
    document.getElementById('moveRight').onclick = function () { move(-0.2); };


