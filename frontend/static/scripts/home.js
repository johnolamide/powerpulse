$(document).ready(() => {
  const url = 'http://0.0.0.0:5000/api/v1/home';
  $.ajax({
    url: url,
    type: 'GET',
    success: (data) => {
      for (let i = 0; i < data.length; i++) {
        let homeBox = $('<div></div>').addClass('homeBox');
        let homeId = $('<h1></h1>').addClass('homeId');
        let temperature = $('<div></div>').addClass('temperature');
        let humidity = $('<div></div>').addClass('humidity');
        let display = $('<section></section>').addClass('display');

        homeId.text('Home ' + data[i].id);
        temperature.text('temp: ' + data[i].temperature + '°C');
        humidity.text('humidity: ' + data[i].humidity);
        let percentage = ((data[i].gen_kw * 100) / data[i].use_kw) * 100;

        // create the donut chart
        let donut = $('<div></div>').addClass('donut');
        donut.css('background', `conic-gradient(#c03221 ${percentage}%,
       #06ba63 ${percentage}% 100%)`);

        // Create the labels
        let label = $('<div></div>').addClass('label');
        let usedLabel = $('<p>Used Energy<p>').attr('id', 'used');
        let unusedLabel = $('<p>Unused Energy</p>').attr('id', 'unused');
        label.append(usedLabel, unusedLabel);
        let description = $('<article></article>').addClass('description');
        let text = $('<p></p>').addClass('text');

        if (percentage > 45) {
          text.text("Energy Usage is too High, conserve energy for the environment");
        } else {
          text.text("Energy Usage is Optimal, keep it up");
        }
        description.append(text);

        let chart = $('<article></article>').addClass('chart');
        chart.append(donut, label);

        let visual = $('<div></div>').addClass('visual');
        visual.append(chart, description);

        homeBox.append(homeId, humidity, temperature);
        display.append(homeId.clone(), visual);

        let article = $('<article></article>');
        article.append(homeBox);
        $('section.homes').append(article);

        article.click(() => {
          $('div.container').html(display);
        });
      };
    },
    error: () => {}
  });
});
