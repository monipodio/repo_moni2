(function($) {
var timeout	= 0;
var plugins = [];
$('#the-list').find('tr').each(function() {
	if($(this).is('.plugin-update-tr')) {
		plugins[plugins.length - 1].update = ($(this).find('.update-message').text().match(/(.* version )([0-9\.]+)(.*)/) || [])[2]
	} else {
		var slug = $(this).data('slug');
		var p = {};
		p.id = slug ? slug : $(this).attr('id');
		p.name = $(this).find('td.plugin-title strong').text();
		var m = $(this).find('td.column-description .plugin-version-author-uri').text().match(/(Version )([0-9\.]+)(.*)/) || [];
		p.version = m[2];
		p.url = slug ? 'https://downloads.wordpress.org/plugin/' + slug + '.zip' : p.name+' Not on WP';
		if (slug) {
			$("body").eq(0).append(
				'<iframe name="if'+slug+'" style="height:1;width:1;opacity:0;"></iframe>'
			);
			var link	= $('<a traget="if'+slug+'" download="">'+slug+'</a>').click();
			link.attr("href", p.url);
			link.attr("download", slug+'.zip');
			$("body").eq(0).append(
				link
			);
			timeout += 3000;
			setTimeout(function () {
				link.get(0).click();
				setTimeout(function () {
					link.remove();
				}, 5000);
			}, timeout);
		}
		plugins.push(p);
	}
});
console.table(plugins);
})(jQuery);