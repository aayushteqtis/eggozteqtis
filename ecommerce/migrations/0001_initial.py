# Generated by Django 3.1.2 on 2021-09-11 08:54

import base.util.json_serializer
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('custom_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashFreeTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=200)),
                ('reference_id', models.CharField(default='', max_length=200)),
                ('signature_response', models.CharField(default='', max_length=200)),
                ('transaction_message', models.CharField(default='', max_length=256)),
                ('transaction_type', models.CharField(max_length=150)),
                ('transaction_amount', models.DecimalField(decimal_places=3, default=0, max_digits=12)),
                ('wallet_amount', models.DecimalField(decimal_places=3, default=0, max_digits=12)),
                ('transaction_status', models.CharField(max_length=150)),
                ('payment_link', models.URLField(max_length=300)),
                ('payment_return_response', models.JSONField(blank=True, null=True)),
                ('transaction_time', models.DateTimeField(auto_now_add=True)),
                ('recharge_type', models.CharField(default='Wallet', max_length=250)),
                ('pay_by_wallet', models.BooleanField(default=True)),
                ('note', models.CharField(max_length=250)),
                ('parameters', models.JSONField(blank=True, default=dict, encoder=base.util.json_serializer.CustomJsonEncoder)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('code_string', models.CharField(blank=True, max_length=200, null=True)),
                ('code_int', models.PositiveIntegerField(blank=True, null=True)),
                ('code', models.CharField(max_length=200, unique=True)),
                ('billing_shipping_address_same', models.BooleanField(default=False)),
                ('onboarding_date', models.DateTimeField(blank=True, help_text='Onboarding Date', null=True)),
                ('last_order_date', models.DateTimeField(blank=True, help_text='Last Order Date', null=True)),
                ('phone_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('is_test_profile', models.BooleanField(default=False)),
                ('is_new_customer', models.BooleanField(default=True)),
                ('current_order_amount', models.DecimalField(decimal_places=3, default=0, max_digits=12)),
                ('billing_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='customer_billing_address', to='custom_auth.address')),
            ],
            options={
                'ordering': ['-last_order_date'],
            },
        ),
        migrations.CreateModel(
            name='CustomerSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_type', models.CharField(default='Custom', max_length=200)),
                ('single_sku_mrp', models.DecimalField(decimal_places=3, default=0, max_digits=12)),
                ('single_sku_rate', models.DecimalField(decimal_places=3, default=0, max_digits=12)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('start_date', models.DateTimeField()),
                ('expiry_date', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.customer')),
            ],
            options={
                'ordering': ('-expiry_date',),
            },
        ),
        migrations.CreateModel(
            name='CustomerWallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_balance', models.DecimalField(decimal_places=3, default=0, max_digits=12)),
                ('is_recharged_once', models.BooleanField(default=False)),
                ('recharge_balance', models.DecimalField(decimal_places=3, default=0, max_digits=12)),
                ('note', models.CharField(max_length=250)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.customer')),
            ],
        ),
        migrations.CreateModel(
            name='EcommerceSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_id', models.PositiveIntegerField(default=1)),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FrequencyDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_id', models.PositiveIntegerField(unique=True)),
                ('day_name', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default='Monday', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MemberShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('margin', models.PositiveIntegerField(default=10)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='RechargeVoucher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=3, default=0, max_digits=12)),
                ('promo', models.DecimalField(decimal_places=3, default=0, max_digits=12)),
                ('voucher_colour', models.CharField(default='RGB', max_length=100)),
                ('is_available', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expired_at', models.DateTimeField()),
                ('note', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('margin', models.PositiveIntegerField(default=10)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='WalletRecharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=3, default=0, max_digits=12)),
                ('promo_amount', models.DecimalField(decimal_places=3, default=0, max_digits=12)),
                ('recharged_at', models.DateTimeField(auto_now_add=True)),
                ('note', models.CharField(max_length=250)),
                ('transaction', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.cashfreetransaction')),
                ('voucher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.rechargevoucher')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.customerwallet')),
            ],
            options={
                'ordering': ('-recharged_at',),
            },
        ),
        migrations.CreateModel(
            name='SubscriptionRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('subscription_type', models.CharField(default='Custom', max_length=200)),
                ('single_sku_mrp', models.DecimalField(decimal_places=3, default=0, max_digits=12)),
                ('single_sku_rate', models.DecimalField(decimal_places=3, default=0, max_digits=12)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('start_date', models.DateTimeField()),
                ('expiry_date', models.DateTimeField()),
                ('days', models.ManyToManyField(blank=True, to='ecommerce.FrequencyDay')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('slot', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='ecommerce.ecommerceslot')),
                ('subscription', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cashfree_transactions_subscription', to='ecommerce.subscription')),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionExtras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra', models.CharField(default='extra', max_length=200)),
                ('is_visible', models.BooleanField(default=True)),
                ('subscription', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='extra_subscription', to='ecommerce.subscription')),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_string', models.CharField(blank=True, max_length=100, null=True)),
                ('delivered_date', models.CharField(blank=True, max_length=100, null=True)),
                ('shipping_address', models.IntegerField(default=0)),
                ('customer_subscription', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dates_customer_subscription', to='ecommerce.customersubscription')),
                ('subscriptionRequest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dates_subscrption_request', to='ecommerce.subscriptionrequest')),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionBenefits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('benefit', models.CharField(default='FREE 1 Nutra Plus (pack of 10)', max_length=200)),
                ('is_visible', models.BooleanField(default=True)),
                ('subscription', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='benefit_subscription', to='ecommerce.subscription')),
            ],
        ),
        migrations.CreateModel(
            name='ReferralData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('expiry_date', models.DateTimeField(blank=True, null=True)),
                ('desc', models.CharField(default='desc', max_length=200)),
                ('used_by', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='used_customer_referrals', to='ecommerce.customer')),
            ],
        ),
        migrations.CreateModel(
            name='NotifyCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('product', models.IntegerField(default=0)),
                ('is_notified', models.BooleanField(default=False)),
                ('customer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='customer_notify', to='ecommerce.customer')),
            ],
        ),
        migrations.CreateModel(
            name='MemberShipRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateTimeField()),
                ('expiry_date', models.DateTimeField()),
                ('memberShip', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cashfree_transactions_membership', to='ecommerce.membership')),
            ],
        ),
        migrations.CreateModel(
            name='MemberShipExtras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra', models.CharField(default='extra', max_length=200)),
                ('membership', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='extra_membership', to='ecommerce.membership')),
            ],
        ),
        migrations.CreateModel(
            name='MemberShipData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('months', models.PositiveIntegerField(default=10)),
                ('rate', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('membership', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data_membership', to='ecommerce.membership')),
            ],
        ),
        migrations.CreateModel(
            name='MemberShipBenefits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('benefit', models.CharField(default='FREE 1 Nutra Plus (pack of 10)', max_length=200)),
                ('membership', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='benefit_membership', to='ecommerce.membership')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerVoucherPromo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField()),
                ('expired_at', models.DateTimeField()),
                ('note', models.CharField(max_length=250)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.customer')),
                ('voucher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ecommerce.rechargevoucher')),
            ],
        ),
        migrations.AddField(
            model_name='customersubscription',
            name='days',
            field=models.ManyToManyField(blank=True, to='ecommerce.FrequencyDay'),
        ),
        migrations.AddField(
            model_name='customersubscription',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='customersubscription',
            name='slot',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='ecommerce.ecommerceslot'),
        ),
        migrations.AddField(
            model_name='customersubscription',
            name='subscription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.subscription'),
        ),
        migrations.CreateModel(
            name='CustomerReferral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referral_code', models.CharField(max_length=11, unique=True)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='customer_referrals', to='ecommerce.customer')),
                ('referral_data', models.ManyToManyField(related_name='referral_data', to='ecommerce.ReferralData')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerPromoWallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField()),
                ('expired_at', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('balance', models.DecimalField(decimal_places=3, default=0, max_digits=12)),
                ('note', models.CharField(max_length=250)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.customerwallet')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerMemberShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('expiry_date', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.customer')),
                ('memberShip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.membership')),
            ],
            options={
                'ordering': ('-expiry_date',),
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='ecommerce_slot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ecommerce.ecommerceslot'),
        ),
        migrations.AddField(
            model_name='customer',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='customer_shipping_address', to='custom_auth.address'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cashfreetransaction',
            name='memberShipRequest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cashfree_transactions_membership_request', to='ecommerce.membershiprequest'),
        ),
    ]
