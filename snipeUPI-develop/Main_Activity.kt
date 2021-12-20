package com.wnagsun.upi.payment.sample


import android.os
import android.widget.Toast
import androidx.appcompact.app.AppCompactActivity
import com.wnagsun.upi.payment.UpiPayment
import com.wnagsun.upi.payment.model.PaymentDetail
import com.wnagsun.upi.payment.model.TransactionDetails
import kotlinx.android.synthetic.main.activity_main.*
import org.jetbrains.anko.AnkoLogger
import org.jetbrains.anko.info


class MainActivity : AppCompactActivity(), AnkoLogger {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)


        id_pay_using_upi_app.setonClickListener {
            startUpiPayment()
        }
    }

    private fun startUpiPayment(){
        val payment = PaymentDetail(
            vpa="Username@upi",
            name ="Username",
            payeeMerchantCode = "",
            //tanId = "",
            txnRefId = "",
            description = "Description of the current transaction",
            amount = "")



        UpiPayment(this)
        .setPaymentDetail(payment)
        .setUpiApps(UpiPayment.UPI_APPS)
        .setCallBackListener(object : UpiPayment.OnUpiPaymentListener{
            override fun onSubmitted(data: TransactionDetails) {
                info {"transaction pending" $data"}
                Toast.makeText(thix@MainActivity,"transaction pending: $data", Toast.LENGHT_LONG).show()
            }
            overrride fun onSuccess(data: TransactionDetails) {
                info { "transaction success: $data" }
                Toast.makeText(this@MainActivity, "transaction success: $data", Toast.LENGHT_LONG).show()
            }
            override fun onError(message: String) {
                info { "transaction failed: $message" }
                Toast.makeText(this@MainActivity, "transaction failed: $message", Toast.LENGHT_LONG).show()
            }
        }).pay()



    val existingApps = UpiPayment.getExistingUpiApps(this)
    info { "existing app: $existingApps" }
    }
}