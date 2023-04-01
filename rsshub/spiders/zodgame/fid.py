from rsshub.spiders.zodgame.zod_info import fid_model_dict,get_zod_module_url,cookie,proxies

from parsel import Selector

from rsshub.utils import DEFAULT_HEADERS,fetch



DEFAULT_HEADERS.update({'cookie': cookie})

domain = 'https://zodgame.xyz'

def parse(post:Selector):
    item = {}
    item['title'] = post.css('.xst').xpath('.//text()').get()
    item['link'] = domain+'/'+post.css('.xst').xpath('.//@href').get()
    item['pubDate'] = post.xpath('.//td[2]/em//span/@title | .//td[2]/em//span/text()').extract_first()
    item['author'] = post.xpath('.//td[2]/cite/a/text()').get()
    #  get post html
    res = fetch(url=item['link'], headers=DEFAULT_HEADERS,proxies=proxies)
    item['description'] = res.css('.pcb').extract_first()
    return item

def ctx(fid:str|int,page:int|str=1):
    # get index html
    url = get_zod_module_url(fid,page)
    
    res = fetch(url=url, headers=DEFAULT_HEADERS,proxies=proxies)
    posts_ = res.css('tbody[id*="normalthread_"]')
    posts = posts_ if len(posts_)<10 else posts_[:10]
    return  {
        'title': f'Zodgame - {fid_model_dict[int(fid)]}',
        'link': get_zod_module_url(fid),
        'description': f'Zodgame - {fid_model_dict[int(fid)]}',
        'author': 'unknown',
        'items': list(map(parse, posts)) 
    }
