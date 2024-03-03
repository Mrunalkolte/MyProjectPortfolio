using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        int gravity = 10;//gravity for falling of the bird
        int pipespeed = 8; //the speed of the pipes to apper
        int score = 0;//initial score
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
           
        }

        public void game_timer(object sender, EventArgs e)
        {
            flappy_bird.Top += gravity; //adding top of the picturebox in gracvity
            pipedown.Left -= pipespeed; //subtracting the pipespeed of the pipes for moving towards left
            pipeup.Left -= pipespeed;
            Scoretext.Text = "Score: " + score;
            if (pipedown.Left < -120) //checking the condition if the pipedwn pitctureboc is less than -120
            {
                pipedown.Left = 800; //then appearing the pipedwn again to make illusion that next pipe is coming
               score++; //score plus for dispay
            }
            if (pipeup.Left < -180)
            {
                pipeup.Left = 900;
                score++;
            }
            if (flappy_bird.Bounds.IntersectsWith(pipedown.Bounds) || flappy_bird.Bounds.IntersectsWith(pipeup.Bounds) 
                || flappy_bird.Bounds.IntersectsWith(pictureBox3.Bounds)||pipeup.Top<-25) //checking if the flappybird pitcture box is touching to the ground or any other pipe and checking if the flappy is not above -25
          {
              endgame();
          }
            if (score > 5) 
            
            {
                pipespeed = 12;//if the score become more than 5 it increases the speed of the pipe dispaying
            }
            
        }

        private void keyisdown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode==Keys.Space) //if the space button is click then
            {
                gravity = -10; //gravity is maintain lessing its gravity by 10 to make it stable
               

            }
        }

        private void Form1_KeyUp(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Space)
            {
                gravity = 10; //gravity is maintain adding its gravity by 10 to make it stable
            }
        }

        private void pictureBox2_Click(object sender, EventArgs e)
        {

        }
        public void endgame()
        {
            timer1.Stop(); //by stoping timer we stop the whole function of the timer so the dispay stucks
            Scoretext.Text += "\n GAME OVER !!";//by += not override what alredy in the score
            
         }
    }
}
