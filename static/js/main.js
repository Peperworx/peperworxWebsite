particlesJS("particles-js", {
  particles: {
    number: {
      value: 180,
      density: {
        enable: true,
        value_area: 800,
      },
    },
    color: {
      value: "#ffffff",
    },
    shape: {
      type: "circle",
      stroke: {
        width: 0,
        color: "#000000",
      },
      polygon: {
        nb_sides: 5,
      },
      image: {
        src: "img/github.svg",
        width: 100,
        height: 100,
      },
    },
    opacity: {
      value: 0.5,
      random: false,
      anim: {
        enable: false,
        speed: 1,
        opacity_min: 0.1,
        sync: false,
      },
    },
    size: {
      value: 3,
      random: true,
      anim: {
        enable: false,
        speed: 40,
        size_min: 0.1,
        sync: false,
      },
    },
    line_linked: {
      enable: true,
      distance: 150,
      color: "#ffffff",
      opacity: 0.4,
      width: 1,
    },
    move: {
      enable: true,
      speed: 6,
      direction: "none",
      random: false,
      straight: false,
      out_mode: "out",
      bounce: false,
      attract: {
        enable: false,
        rotateX: 600,
        rotateY: 1200,
      },
    },
  },
  interactivity: {
    detect_on: "canvas",
    events: {
      onhover: {
        enable: true,
        mode: "grab",
      },
      onclick: {
        enable: true,
        mode: "push",
      },
      resize: true,
    },
    modes: {
      grab: {
        distance: 140,
        line_linked: {
          opacity: 1,
        },
      },
      bubble: {
        distance: 400,
        size: 40,
        duration: 2,
        opacity: 8,
        speed: 3,
      },
      repulse: {
        distance: 200,
        duration: 0.4,
      },
      push: {
        particles_nb: 4,
      },
      remove: {
        particles_nb: 2,
      },
    },
  },
  retina_detect: true,
});

/* ---- stats.js config ---- */

var count_particles, stats, update;

count_particles = document.querySelector(".js-count-particles");
update = function () {
  if (window.pJSDom[0].pJS.particles && window.pJSDom[0].pJS.particles.array) {
    //count_particles.innerText = window.pJSDom[0].pJS.particles.array.length;
  }
  requestAnimationFrame(update);
};
requestAnimationFrame(update);

function getHomepage() {
  var dta = {};
  $.get("https://dev.peperworx.com/strapi/homepage", function (data) {
    dta = data;
  });
  return dta;
}

var header = new Vue({
  el: "#header",
  delimiters: ["[%", "%]"],
  data: {
    nav1: {
      text: "",
      link: "",
    },
    nav2: {
      text: "",
      link: "",
    },
  },
  methods: {
    update: function () {
      var hc = getHomepage();
      this.nav1.text = hc["Nav1Text"] ?? "Home";
      this.nav1.link = hc["Nav1Link"] ?? "#home";
      this.nav2.text = hc["Nav2Text"] ?? "Our Services";
      this.nav2.link = hc["Nav2Link"] ?? "#games";
    },
    togglebtn1: function (event) {
      event.preventDefault();
      console.log("Clicked");

      $("#ourGamesPage").hide("slide", { direction: "right" });

      $("#homePage").show("slide", { direction: "left" });
      $("[href='#games']").toggleClass("active");
      $("[href='#home']").toggleClass("active");
    },
    togglebtn2: function (event) {
      event.preventDefault();
      console.log("Clicked");

      $("#ourGamesPage").show("slide", { direction: "right" });

      $("#homePage").hide("slide", { direction: "left" });

      $("[href='#games']").toggleClass("active");
      $("[href='#home']").toggleClass("active");
    },
  },
});

var main = new Vue({
  el: "#main",
  delimiters: ["[%", "%]"],
  data: {
    button1: {
      text: "",
      link: "",
      display: "inline",
    },
    button2: {
      text: "",
      link: "",
      display: "none",
    },
    box1: {
      text: "",
    },
    box2: {
      text: "",
    },
  },
  methods: {
    update: function () {
      var hc = getHomepage();

      this.button1.text = hc["Button1Text"] ?? "";
      this.button1.link = hc["Button1Text"] ?? "";
      this.button1.display = hc["Button1Text"] ? "inline" : "none";
      this.button2.text = hc["Button2Text"] ?? "";
      this.button2.link = hc["Button2Text"] ?? "";
      this.button2.display = hc["Button2Text"] ? "inline" : "none";
      this.box1.text = hc["box1"] ?? "";
      this.box2.text = hc["box2"] ?? "";
    },
  },
});
header.update();
main.update();

$("[href='#home']").click(function (event) {});

$("[href='#games']").click(function (event) {});
