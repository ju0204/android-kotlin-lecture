package com.example.animation

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.view.ViewGroup
import androidx.transition.AutoTransition
import androidx.transition.Scene
import androidx.transition.Transition
import androidx.transition.TransitionManager
import com.example.animation.databinding.ActivityTransitionBinding

class TransitionActivity : AppCompatActivity() {
    private lateinit var binding: ActivityTransitionBinding
    private lateinit var scene1: Scene
    private lateinit var scene2: Scene

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivityTransitionBinding.inflate(layoutInflater)
        setContentView(binding.root)
        scene1 = Scene.getSceneForLayout(binding.sceneRoot, R.layout.scene_1, this)
        scene2 = Scene.getSceneForLayout(binding.sceneRoot, R.layout.scene_2, this)
    }

    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate(R.menu.transition_menu, menu)
        return super.onCreateOptionsMenu(menu)
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        when (item.itemId) {
            R.id.scene_1 -> TransitionManager.go(scene1)
            R.id.scene_2 -> TransitionManager.go(scene2)
        }
        return super.onOptionsItemSelected(item)
    }
}