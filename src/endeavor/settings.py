BOT_NAME = 'endeavor'

SPIDER_MODULES = ['endeavor.spiders']
NEWSPIDER_MODULE = 'endeavor.spiders'

ROBOTSTXT_OBEY = True

LOG_LEVEL = 'INFO'

ITEM_PIPELINES = {
    'endeavor.pipelines.ShipItemPipeline': 300,
}

MONGO_URL = 'mongodb+srv://akiya:Ae49GpfAjRmHD1CG' + \
    '@cluster.1impi.mongodb.net/DEV?retryWrites=true&w=majority'
