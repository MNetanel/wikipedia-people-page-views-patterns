# Ideas
1. Can we predict a country's view on a subject by analyzing wikipedia *attention* and *coverage* pattern?
	1. For example, Israel:
		1. [International recognition of Israel - Wikipedia](https://en.wikipedia.org/wiki/International_recognition_of_Israel)
		2. [International Opinion Toward Israel](https://www.jewishvirtuallibrary.org/international-opinion-toward-israel)
		3. [Transatlantic Trends Survey Series](https://www.icpsr.umich.edu/web/ICPSR/series/235/publications)
2.  Or: Can the amount of *attention* and *coverage* a country gives to Israel predict the attitude towards it?
	1. For example, @ruprechterPoorAttentionWealth2023 : *"We find that major Wikipedia language editions have a skewed focus, with more attention given to events in the world’s more economically developed countries and less attention to events in less affluent regions. However, other factors, such as the number of deaths in a disaster, are also associated with the attention an event receives."*
3. Or: can it predict the sentiment in the article?
4. What is *attention*?
	1. *Attention* = Page views
	2. Page views of related pages (could be positive or negative attention)
	3. *Coverage* = Number of edits

https://chat.openai.com/share/35ce5efa-fb76-4dde-9c44-c5026718a26a
# Countries and Languages


# Previous Works
https://arxiv.org/pdf/2305.09497.pdf


# Methods
* See @ruprechterPoorAttentionWealth2023 repo: [GitHub - ruptho/wiki-event-bias: Repository for "Poor attention: The wealth and regional gaps in event attention and coverage on Wikipedia" as published in PONE.](https://github.com/ruptho/wiki-event-bias)
* See Pudding.cool's [Life After Death on Wikipedia](https://pudding.cool/2018/08/wiki-death/) repo: [GitHub - the-pudding/wiki-death-data](https://github.com/the-pudding/wiki-death-data/tree/master)
* [(Open Access) Wikipedia traffic data and electoral prediction: towards theoretically informed models (2015) | Taha Yasseri | 6 Citations](https://typeset.io/papers/wikipedia-traffic-data-and-electoral-prediction-towards-1l0m91908g)

# Tools
- https://pyts.readthedocs.io/en/stable/auto_examples/transformation/plot_shapelet_transform.html
- https://github.com/MaxBenChrist/awesome_time_series_in_python?tab=readme-ov-file

# Data
* X:
  * https://github.com/GeneralMills/pytrends
  * [Pageview complete dumps](https://dumps.wikimedia.org/other/pageview_complete/readme.html)
  * wikipedia rest api
* y:
  * https://global100.adl.org/map

# Questions?
- Which pages to analyze?
	- Obviously we cannot analyze every single page (that would have >300GB of data)
	- Only pages from https://en.wikipedia.org/wiki/Wikipedia:Popular_pages

# Future Work
- Mixture of multiple patterns
- How patterns of related pages relate to/affect each other