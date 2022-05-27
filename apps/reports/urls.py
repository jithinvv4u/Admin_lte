from django.urls import path
from .views import getPiechartWallet, getfilterNotify, getfilterOrderWallet, getfilterReferrals, getfilterStock,getfilterSettlement, getfilterUser, load_cities, newUser, order_wallet_trans, settlement_report, stock_in_hand_view, user_referral_report, veg_price_view,wallet_transaction_view,notify_report_view,getfilterWallet,getfilterVeg,veg_inv_sale_report,daily_sale_report

urlpatterns = [

    path('reports/veg_price/',veg_price_view,name='veg_price'),
    path('filter_vegitble/',getfilterVeg),
    
    path('reports/wallet/',wallet_transaction_view,name='wallet_transaction'),
    path('filter_wallet/',getfilterWallet),
    
    path('reports/notify_report/',notify_report_view,name='notify_report'),
    path('filter_notify/',getfilterNotify),
    
    path('reports/stock_in_hand/',stock_in_hand_view,name='stock_in_hand'),
    path('filter_stock/',getfilterStock),
    
    path('reports/referral/',user_referral_report,name='referral'),
    path('filter_referrals/',getfilterReferrals),
    
    path('reports/order_wallet',order_wallet_trans,name='order_wallet'),
    path('filter_order_wallet/',getfilterOrderWallet),
    path('wallet_piechart/',getPiechartWallet),
    
    path('reports/settlement_report/',settlement_report,name='settlement'),
    path('filter_settlement/',getfilterSettlement),
    path('select_cities/',load_cities),
    
    path('reports/new_user_report/',newUser,name='new_user'),
    path('filter_newUser/',getfilterUser),
    
    
]
