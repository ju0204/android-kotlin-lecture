package com.example.customview

import android.content.Context
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import android.graphics.Typeface
import android.util.AttributeSet
import android.view.View

class MyCanvas : View {
    private val paint = Paint()

    constructor(context: Context) : super(context)
    constructor(context: Context, attrs: AttributeSet) : super(context, attrs)

    override fun onDraw(canvas: Canvas) {
        super.onDraw(canvas)

        // fill background with the color
        canvas.drawColor(Color.YELLOW)

        // draw a line
        paint.color = Color.RED
        paint.strokeWidth = 5F
        canvas.drawLine(100F, 100F, 500F, 200F, paint)

        paint.reset()
        // draw a circle
        paint.color = Color.BLUE
        canvas.drawCircle(200F, 200F, 100F, paint)

        paint.strokeWidth = 5F
        paint.style = Paint.Style.STROKE  // draw a line only without filling
        canvas.drawRect(500F, 200F, 600F, 300F, paint)

        paint.textSize = 50F
        paint.typeface = Typeface.SERIF
        canvas.drawText("Hello", 100F, 350F, paint)
    }
}
