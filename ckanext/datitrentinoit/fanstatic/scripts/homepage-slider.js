/**
 * Header Image roll effect
 * Author: Samuele Santi
 * Date: 2012-11-21
 * Time: 11:17 AM
 */

$(document).ready(function(){

    var conf = {
        fadeTime: 0,
        rollTime: 4000
    };

    var rollImageInit = function(imgroll) {
        imgroll.children().each(function(idx,item){
            if (idx==0) {
                $(item).show();
            }
            else {
                $(item).hide();
            }
        });
    };

    var rollImageNext = function(imgroll) {
        var imgidx = imgroll.data('rollimg-idx') || 0,
            imgcount = imgroll.children().length,
            nextidx = (imgidx + 1) % imgcount,
            oldimg = $(imgroll.children()[imgidx]),
	    bgimg = null;

        imgroll.children().each(function(idx,item){
            if (idx==imgidx) {
                $(item).show().css('z-index', '2');
            }
            else if (idx==nextidx) {
                $(item).show().css('z-index', '1');
		bgimg = $(item).data('bgimage');
            }
            else {
                $(item).hide();
            }
        });

        // To allow attaching extra handlers
        $(imgroll).trigger('roll-start', {
            target: $(imgroll.children()[nextidx]),
            conf: conf
        });

        oldimg.fadeOut(conf.fadeTime);
	$(imgroll).parent('.hero').css('background-image', 'url(/images/home-slider/'+bgimg+')');
	$('.hero').css('background-image', 'url(/images/home-slider/'+bgimg+')');
        imgroll.data('rollimg-idx', nextidx);
    };

    $('.home-slider-container').each(function(){
        var imgroll = $(this);

        imgroll.css({
            'position': 'relative'
        });
        imgroll.children().css({
            "position": "absolute",
            "top": 0,
            "left": 0,
            "right": 0,
        });

        rollImageInit(imgroll);
        setInterval(function(){
            rollImageNext(imgroll);
        }, conf.rollTime);
    });

});
