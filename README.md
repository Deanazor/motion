# Motion Tracking

This is a simple GUI-based application to track motion

## How to run

Clone repository :

```bash
  git clone https://github.com/Deanazor/ndflx1.git
```

Go to repository folder :

```bash
  cd ndflx1
```

I recommend you to pull this repository to make it easier to run the application later

Build docker image :

```bash
  docker build -t deanazor/motion .
```

Or, you can simply pull the image :

```bash
  docker pull deanazor/motion
```

There is some few steps before we can run the docker image, but I've made a shell script to make it easier for you to run the docker image (which is why I recommend you to clone this repository)

Run image :

```bash
  sh runDocker.sh
```

After the GUI pop up, you can press "T" to take background picture, "P" to start tracking, "S" to stop tracking, and "Esc" key to close application

## Background and Motion Example
### Background
![Input](./Foto/cap_1.png)
### Motion detected
![Output](./Foto/cap_2.png)