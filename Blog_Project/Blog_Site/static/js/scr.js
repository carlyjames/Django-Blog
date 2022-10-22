

$(document).ready(function () {
    $('[data-class]').click(function () {
        updateNavbarClass($(this).attr('data-class'));
    });

    updateNavbarClass('fixed-left');

    themes.forEach(function (theme) {
        $('#theme_select').append($('<option>', {
            value: theme,
            text: theme.charAt(0).toUpperCase() + theme.slice(1),
            selected: theme === 'material'
        }));
    });
});

function updateNavbarClass(className) {
    $('nav')
        .removeClass(function (index, css) {
            return (css.match(/(^|\s)fixed-\S+/g) || []).join(' ');
        })
        .addClass(className);

    $('[data-class]').removeClass('active').parent('li').removeClass('active');
    $('[data-class="' + className + '"]').addClass('active').parent('li').addClass('active');

    fixBodyMargin(className);
}

function fixBodyMargin(className) {
    if (/fixed-(left|right)/.test(className)) {
        $('body').removeAttr('style');
        if (className === 'fixed-right') {
            $('body').css('marginLeft', 0);
        } else {
            $('body').css('marginRight', 0);
        }
    } else {
        $('body').css({
            "margin-right": 0,
            "margin-left": 0,
            "padding-top": '0px'
        });
    }
}

function selectTheme(theme) {
    $('#theme_link').attr('href', 'https://cdnjs.cloudflare.com/ajax/libs/bootswatch/4.3.1/' + theme + '/bootstrap.min.css');
}

var form = document.getElementById("myForm");
function handleForm(event) { event.preventDefault(); } 
form.addEventListener('submit', handleForm);


window.onscroll = function() {
	var e = document.getElementById("scrolltop");
    if (!e) {
    	e = document.createElement("a");
        e.id = "scrolltop";
        e.href = "#";
        document.body.appendChild(e);
	}
	e.style.display = document.documentElement.scrollTop > 300 ? "block" : "none";
    e.onclick = (ev) => {
    	ev.preventDefault();
        document.documentElement.scrollTop = 0;
    };
};





