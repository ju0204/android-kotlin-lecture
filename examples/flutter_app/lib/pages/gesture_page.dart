import 'package:flutter/material.dart';

class _State extends State<GesturePage> {
  bool _lightIsOn = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(GesturePage.menu_name)),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(
              Icons.lightbulb_outline,
              color: _lightIsOn ? Colors.yellow.shade600 : Colors.black,
              size: 60,
            ),
            GestureDetector(
              onTap: () {
                setState(() {
                  _lightIsOn = !_lightIsOn;
                });
              },
              child: Text(_lightIsOn ? 'TURN LIGHT OFF' : 'TURN LIGHT ON',
                  style: TextStyle(backgroundColor: Colors.amber)),
            ),
          ],
        ),
      ),
    );
  }
}

class GesturePage extends StatefulWidget {
  static const nav_url = '/gesture';
  static const menu_name = 'Gesture Page';

  @override
  _State createState() => _State();
}
