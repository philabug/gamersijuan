$(function(){
    
    $("#search").click(function() {
        $("#result").show(); 
    });

    $(document).mouseup(function (e) { 
        if ($(e.target).closest("#search-content").length 
                    === 0) { 
            $("#result").hide(); 
        } 
    }); 

    ///////////////// fixed menu on scroll for desktop
    if ($(window).width() > 992) {
        $(window).scroll(function(){  
        if ($(this).scrollTop() > 40) {
            $('#navbar_top').addClass("fixed-top");
            // add padding top to show content behind navbar
            $('body').css('padding-top', $('.navbar').outerHeight() + 'px');
            }else{
            $('#navbar_top').removeClass("fixed-top");
            // remove padding top from body
            $('body').css('padding-top', '0');
            }   
        });
    } //end if
    
    // dark mode
    var darkMode;

    if (localStorage.getItem('dark-mode')) {  
        // if dark mode is in storage, set variable with that value
        darkMode = localStorage.getItem('dark-mode');  
    } else {  
        // if dark mode is not in storage, set variable to 'light'
        darkMode = 'light';  
    }

    // set new localStorage value
    localStorage.setItem('dark-mode', darkMode);

    // apply dark/light mode
    if (localStorage.getItem('dark-mode') == 'dark') {
        $('body').addClass('dark');  
        $('#right-menu').after('<div class="custom-control custom-switch">'+
                '<input type="checkbox" class="custom-control-input" id="darkmodeSwitch" checked="checked">'+
                '<label class="custom-control-label" for="darkmodeSwitch">Dark Mode</label></div>'
        )
        $('nav').css('background-color','#383838')
        $('.pagination').css('background-color','#222')
        $('footer').css('background-color','#383838')
        $('.card-body').css('background-color','#383838')
        $('hr').css({'border-top': '1px solid #dee2e6','opacity': '0.1'})   
    }else{
        $('#right-menu').after('<div class="custom-control custom-switch">'+
                '<input type="checkbox" class="custom-control-input" id="darkmodeSwitch" unchecked>'+
                '<label class="custom-control-label" for="darkmodeSwitch">Dark Mode</label></div>'
        )
        $('nav').css('background-color','#e9ecef ')
        $('.pagination').css('background-color','#fff')
        $('footer').css('background-color','#e9ecef')
        $('card').css('border','1px solid gray')
        $('hr').css({'border-top': '1px solid #000000','opacity': '0.1'}) 
    }
    
    $('#darkmodeSwitch').change(function() {
        if(this.checked) {
            $('body').addClass('dark');  
            localStorage.setItem('dark-mode', 'dark');
            
            $('nav').css('background-color','#383838')
            $('.pagination').css('background-color','#222')
            $('footer').css('background-color','#383838')
            $('.card-body').css('background-color','#383838')
            $('hr').css({'border-top': '1px solid #dee2e6','opacity': '0.1'})   
        }else{
            $('body').removeClass('dark');
            localStorage.setItem('dark-mode','light');

            $('nav').css('background-color','#e9ecef ')
            $('.pagination').css('background-color','#fff')
            $('footer').css('background-color','#e9ecef')
            $('card').css('border','1px solid gray')
            $('.card-body').css('background-color','#fff')
            $('hr').css({'border-top': '1px solid #000000','opacity': '0.1'})  
        }   
    });
    // end dark mode


})

