//  https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=378394338d6286ca59ed96d25cf8f8db

var img_prefix_url = 'https://image.tmdb.org/t/p/original';
var api_call_url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=378394338d6286ca59ed96d25cf8f8db';

debugger;
$(document).ready(function(){
    $('.best-films-spinner').show();

  $.ajax({
          url: api_call_url,
          success: function(result){
                console.log(result);

                if (result.results.length > 0){
                    $('.best-films').html('');
                    $('.best-films-spinner').hide();
                }
                var i = 1;
                result.results.forEach(function(r){
                    // console.log(r.original_title);
                    // console.log(img_prefix_url + r.poster_path);

                    var html = `<div class="col-sm-3">
                                    <div class="card" style="width: 18rem;">
                                        <img src="`+ img_prefix_url + r.poster_path +`" class="card-img-top" alt="...">
                                        <div class="card-body">
                                            <h5 class="card-title">
                                                `+r.original_title+ `
                                                <span class="badge bg-secondary">` + i + `</span>
                                            </h5>
                                            <p class="card-text"></p>
                                            <a href="#" class="btn btn-primary">POPULARITAT  <span class="badge bg-secondary">` + r.popularity + `</span></a>
                                        </div>
                                    </div>
                                </div>`;

                    $('.best-films').append(html)
                    i++;
                    // r.original_title
                    // r.poster_path
                });

          }
      });

});