import stripe
stripe.api_key = "sk_test_N90VIt5oyKlvO5A3cszKznIr"

def createCharge(num,token,info):
    try:
        charge = stripe.Charge.create(
            amount = num,
            currency = "usd",
            source = token,
            description = info
        )
    except stripe.error.CardError, e:
        pass

