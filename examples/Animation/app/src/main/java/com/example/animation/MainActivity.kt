package com.example.animation

import android.animation.AnimatorInflater
import android.animation.AnimatorSet
import android.animation.ObjectAnimator
import android.animation.ValueAnimator
import android.content.Intent
import android.graphics.drawable.AnimationDrawable
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.view.animation.AccelerateInterpolator
import android.view.animation.LinearInterpolator
import com.example.animation.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        binding.startAnimation.setOnClickListener {
            startAnimation()
            startAnimatorSet()
            startXMLAnimator()
        }
    }

    private fun startAnimation() {
        // 1. Drawable Animation

        // DO NOT set the bitmap of the imageView
        binding.imageView.setBackgroundResource(R.drawable.moving_circle)
        // or set the background of the imageView as @drawable/moving_circle in XML
        val animation = binding.imageView.background as AnimationDrawable
        animation.stop()
        animation.start()

        // 2. Value Animator
        ValueAnimator.ofFloat(0f, 200f).apply {
            duration = 2000
            addUpdateListener { updatedAnimation ->
                binding.tvValueAnimator.text = "${updatedAnimation.animatedValue as Float}"
                binding.tvValueAnimator.translationX = updatedAnimation.animatedValue as Float
            }
            start()
        }

        // 3. Object Animator
        ObjectAnimator.ofFloat(binding.tvObjectAnimator, "translationX", 0f, 200f).apply {
            duration = 2000
            interpolator = AccelerateInterpolator()
            start()
        }
    }

    private fun startAnimatorSet() {
        binding.tvAnimatorSet.alpha = 1.0f
        val ani1 = ObjectAnimator.ofFloat(binding.tvAnimatorSet, "translationX", 0f, 200f).apply {
            duration = 1500
        }
        val ani2 = ObjectAnimator.ofFloat(binding.tvAnimatorSet, "translationY", 0f, 200f).apply {
            duration = 1500
        }
        val fadeAnim = ObjectAnimator.ofFloat(binding.tvAnimatorSet, "alpha", 1f, 0f).apply {
            duration = 500
        }
        AnimatorSet().apply {
            play(ani1).with(ani2)
            play(fadeAnim).after(ani1)
            // playTogether()
            // playSequentially()
            start()
        }
    }

    private fun startXMLAnimator() {
        binding.tvXMLAnimator.alpha = 1.0f
        (AnimatorInflater.loadAnimator(this, R.animator.animator_xml) as AnimatorSet).apply {
            setTarget(binding.tvXMLAnimator)
            start()
        }
    }

    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate(R.menu.main_menu, menu)
        return super.onCreateOptionsMenu(menu)
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        when (item.itemId) {
            R.id.transition -> startActivity(
                Intent(this, TransitionActivity::class.java)
            )
            R.id.motionLayout -> startActivity(
                Intent(this, MotionActivity::class.java)
            )
        }
        return super.onOptionsItemSelected(item)
    }
}