$(document).ready(function () {
  $(".banner-carousel").owlCarousel({
    animateOut: "fadeOut",
    animateIn: "flipInX",
    items: 1,
    smartSpeed: 450,
    nav: true,

    loop: true,
    dots: false,
    mouseDrag: false,
    touchDrag: false,
  });

  $(".team-carousel").owlCarousel({
    loop: true,
    margin: 50,
    autoplay: true,
    responsive: {
      0: {
        items: 1,
      },
      600: {
        items: 2,
      },
      1000: {
        items: 3,
      },
    },
  });

  $(".overlay-gallery").magnificPopup({
    delegate: "a",
    type: "image",
    closeMarkup:
      '<button  class="mfp-close" style=" right: 8px"><img src="static/images/close.png" class="mfp-close" style="width:50px;height:50px"/></button>',

    gallery: {
      enabled: true,

      arrowMarkup:
        '<img class="mfp-arrow custom-mfp-arrow-%dir%" src="static/images/arrow.png" style="margin:0"/>',

      tPrev: "Previous",
      tNext: "Next",
      tCounter:
        '<span  style="color:red; font-size:17px" class="mfp-counter">%curr% of %total%</span>',
    },

    zoom: {
      enabled: true,
      duration: 300,
      easing: "ease-in-out",
      opener: function (openerElement) {
        return openerElement.is("img")
          ? openerElement
          : openerElement.find("img");
      },
    },
  });

  $(".pics").magnificPopup({
    delegate: "a",
    type: "image",
    closeMarkup:
      '<button  class="mfp-close" style=" right: 8px"><img src="../static/images/close.png" class="mfp-close" style="width:50px;height:50px"/></button>',

    gallery: {
      enabled: true,
      arrowMarkup:
        '<img class="mfp-arrow custom-mfp-arrow-%dir%" src="../static/images/arrow.png" style="margin:0"/>',

      tPrev: "Previous",
      tNext: "Next",
      tCounter:
        '<span  style="color:red; font-size:17px" class="mfp-counter">%curr% of %total%</span>',
    },
    zoom: {
      enabled: true,
      duration: 300,
      easing: "ease-in-out",
      opener: function (openerElement) {
        return openerElement.is("img")
          ? openerElement
          : openerElement.find("img");
      },
    },
  });

  $(".register-icon").magnificPopup({
    type: "inline",
    preloader: true,
		focus: '#focus',
    mainClass: 'mfp-fade',
    closeMarkup:
      '<button  class="mfp-close" style=" right: 8px;top:-1.5em"><img src="../static/images/close.png" class="mfp-close" style="width:50px;height:50px"/></button>',
    
  });

  $(".login-icon").magnificPopup({
    type: "inline",
    preloader: true,
		focus: '#focus',
    mainClass: 'mfp-fade',
    closeMarkup:
      '<button  class="mfp-close" style=" right: 8px;top:-1.5em"><img src="../static/images/close.png" class="mfp-close" style="width:50px;height:50px"/></button>',   
  });

setTimeout(function(){
  $('#message').fadeOut('slow');
}, 3000);

  var Class1 = "تی آر ایکس";
  var Class2 = "بدنسازی";
  var Class3 = "فیتنس";
  var Class4 = "بادی پامپ";
  var Class5 = "یوگا";
  var Class6 = "اسپینیگ";

  $(".Class1").append(Class1);
  $(".Class2").append(Class2);
  $(".Class3").append(Class3);
  $(".Class4").append(Class4);
  $(".Class5").append(Class5);
  $(".Class6").append(Class6);

  $(".menu").click(function () {
    $(".pages").toggleClass("active");
  });

  $("#close").on("click", function () {
    $.magnificPopup.close();
  });

  $(function () {
    var selectedClass = "";
    $(".filter").click(function () {
      selectedClass = $(this).attr("data-rel");
      if (selectedClass == "all") {
        $(".gallery-item").addClass("pics").removeClass("filter-gallery");
      } else {
        $(".gallery-item").addClass("filter-gallery").removeClass("pics");
      }
      $("#gallery").fadeTo(100, 0.1);
      $("#gallery div")
        .not("." + selectedClass)
        .fadeOut()
        .removeClass("animation");
      setTimeout(function () {
        $("." + selectedClass)
          .fadeIn()
          .addClass("animation");
        $("#gallery").fadeTo(300, 1);
      }, 300);
    });
  });

  $(".timetable-controls ul li").on("click", function () {
    var tsfilter = $(this).data("tsfilter");
    $(".timetable-controls ul li").removeClass("active");
    $(this).addClass("active");

    if (tsfilter == "all") {
      $(".classtime-table").removeClass("filtering");
    } else {
      $(".classtime-table").addClass("filtering");
    }
    $(".ts-item").each(function () {
      $(this).removeClass("show");
      if ($(this).data("tsmeta") == tsfilter) {
        $(this).addClass("show");
      }
    });
  });
});
